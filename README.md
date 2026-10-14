# Camino Selva · Estilo e identidad visual

Recursos de marca, referencias de diseño y skill reutilizable de Camino Selva, mantenidos en la organización **CEE-ENRIQUEZ**.

## Descargar solamente la skill

**[Descargar camino-selva-brand.zip](https://github.com/CEE-ENRIQUEZ/camino-selva-estilo/releases/latest/download/camino-selva-brand.zip)**

Ingresar a GitHub con una cuenta que tenga acceso a este repositorio privado. El enlace descarga el paquete de la skill, con su carpeta `camino-selva-brand/` y sus referencias. No hace falta descargar todos los originales de marca.

1. Guardar `camino-selva-brand.zip` en una carpeta corta, por ejemplo `C:\Skills`.
2. Hacer clic derecho en el ZIP y elegir **Extraer todo**.
3. Conservar completa la carpeta `camino-selva-brand` extraída; contiene `SKILL.md`, `assets`, `references` y `agents`.

Alternativa: abrir [el ZIP guardado en el repositorio](output/skills/camino-selva-brand.zip) y pulsar **Download raw file**. **Code → Download ZIP** descarga el repositorio completo, incluido el material de diseño.

### Si aparece «ruta de acceso demasiado larga»

Las descargas completas anteriores al 14 de octubre de 2026 incluían rutas de originales de hasta 207 caracteres, antes de sumar la carpeta de destino. La estructura actual usa nombres cortos y conserva el contenido de los 146 originales, con su correspondencia en [originales/manifest.json](originales/manifest.json).

Volver a descargar el archivo actualizado o usar el enlace de la skill de arriba. Para un ZIP anterior, extraerlo en una carpeta corta reduce la longitud total de la ruta. Esta corrección no requiere cambiar la configuración de Windows.

## Contenido

- `skills/camino-selva-brand/`: skill con instrucciones, referencias, tokens CSS/JSON y logos SVG.
- `originales/`: originales de marca en los formatos entregados, con rutas cortas. [Catálogo y correspondencias](originales/README.md).
- `Camino selva - Ajustes Anteproyecto.pdf`: anteproyecto de identidad visual de Diseño Shakespear.
- `output/skills/camino-selva-brand.zip`: paquete portable de la skill.
- `output/skills/camino-selva-brand-before-figma-2026-10-01.zip`: respaldo anterior a la incorporación del Design System.

## Referencias para implementación web

La skill incorpora la revisión del **1 de octubre de 2026** del [Design System de Figma](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=587-8018), incluyendo Inter y Space Grotesk, colores semánticos, componentes, menús y reglas mobile.

Entradas principales:

- [Instrucciones de la skill](skills/camino-selva-brand/SKILL.md).
- [Design System y procedencia de los valores](skills/camino-selva-brand/references/figma-design-system.md).
- [Integración y migración de tokens](skills/camino-selva-brand/references/digital-use.md).
- [Estructura de los menús desktop](skills/camino-selva-brand/references/desktop-menus.md).
- [Tokens JSON](skills/camino-selva-brand/assets/brand-tokens.json) y [variables CSS](skills/camino-selva-brand/assets/brand-tokens.css).

La carpeta de la skill es autónoma y se puede copiar completa o distribuir mediante el ZIP. Los archivos de fuentes y la biblioteca completa de Figma no están incluidos. Las revisiones y discrepancias documentadas corresponden a las fuentes conservadas; no representan una sincronización automática con Figma ni una certificación de la web implementada.

## Mantenimiento

Los originales conservan su procedencia. Aplicar las instrucciones y materiales finales más recientes del proyecto al elegir recursos. Actualizar el paquete ZIP cuando se modifique la skill.

Antes de publicar una actualización, ejecutar `python scripts/check_distribution.py`. Comprueba longitudes de rutas, integridad de los ZIP y hashes de los originales; el límite preventivo del repositorio deja espacio para la carpeta de descarga de Windows.

La carpeta `tmp/`, el respaldo local con los nombres largos anteriores y los metadatos del sistema operativo quedan fuera del repositorio. Los PDFs, recursos originales y paquetes de distribución se versionan.
