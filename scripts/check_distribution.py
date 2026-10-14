"""Check Windows download paths and preserved brand files; standard library only."""

from pathlib import Path, PurePosixPath
import hashlib
import json
import subprocess
import zipfile


ROOT = Path(__file__).resolve().parents[1]
# Project limits, not Windows OS limits: reserve space for the download directory.
MAX_REPO_PATH = 100
MAX_SKILL_ZIP_PATH = 80


def checked_path(name, limit):
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '\\' in name:
        raise ValueError(f'Unsafe archive path: {name}')
    if len(name) > limit:
        raise ValueError(f'Path exceeds {limit} characters ({len(name)}): {name}')
    for part in path.parts:
        if any(char in part for char in '<>:"|?*') or part.endswith((' ', '.')):
            raise ValueError(f'Invalid Windows path component: {name}')


def main():
    # The index includes staged renames before publishing; ignored local backups stay out.
    raw = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT)
    names = [name for name in raw.decode('utf-8').split('\0') if name]
    if not names:
        raise ValueError('No tracked files')
    for name in names:
        checked_path(name, MAX_REPO_PATH)
        if not (ROOT / name).is_file():
            raise ValueError(f'Tracked file missing: {name}')

    manifest = json.loads((ROOT / 'originales/manifest.json').read_text(encoding='utf-8'))
    listed = set()
    for entry in manifest['files']:
        name = entry['path']
        checked_path(name, MAX_REPO_PATH)
        if not name.startswith('originales/') or name.casefold() in listed:
            raise ValueError(f'Unexpected or duplicate original path: {name}')
        listed.add(name.casefold())
        actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        if actual != entry['sha256']:
            raise ValueError(f'Original content changed: {name}')
    originals = {name.casefold() for name in names if name.startswith('originales/') and Path(name).suffix.lower() in {'.ai', '.svg', '.png', '.jpg'}}
    if originals != listed:
        raise ValueError('Original file inventory differs from the manifest')

    zip_max = 0
    for package in sorted((ROOT / 'output/skills').glob('*.zip')):
        with zipfile.ZipFile(package) as archive:
            entries = archive.namelist()
            if len(entries) != len({entry.casefold() for entry in entries}):
                raise ValueError(f'Duplicate ZIP entries: {package.name}')
            for entry in entries:
                checked_path(entry, MAX_SKILL_ZIP_PATH)
                if PurePosixPath(entry).parts[0] != 'camino-selva-brand':
                    raise ValueError(f'Unexpected skill root: {entry}')
            if 'camino-selva-brand/SKILL.md' not in entries:
                raise ValueError(f'Missing skill entrypoint: {package.name}')
            if archive.testzip() is not None:
                raise ValueError(f'Corrupt ZIP: {package.name}')
            zip_max = max(zip_max, max(map(len, entries)))
    if not zip_max:
        raise ValueError('No skill ZIP packages found')
    print(f'OK: {len(names)} repository files; longest relative path {max(map(len, names))} characters.')
    print(f'OK: {len(listed)} original assets match their SHA-256 hashes.')
    print(f'OK: skill ZIP integrity; longest entry path {zip_max} characters.')


if __name__ == '__main__':
    main()
