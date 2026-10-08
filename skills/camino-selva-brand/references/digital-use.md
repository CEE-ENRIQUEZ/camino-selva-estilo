# Aplicación a interfaces digitales

Leer [el Design System de Figma](figma-design-system.md): es la referencia actual para web, por indicación del usuario. Reemplaza las propuestas anteriores de composición, tipografías de interfaz, espaciado y componentes. El [anteproyecto](brand-guide.md) conserva geometría histórica y usos de otros soportes; la [lámina de septiembre](web-palette.md) queda como antecedente de color.

## Integración

Copiar al proyecto solo los recursos que use. No depender en ejecución de una carpeta personal de skills ni publicar PDFs de referencia dentro del bundle web. Adaptar [brand-tokens.json](../assets/brand-tokens.json) al sistema de tokens del proyecto y usar [brand-tokens.css](../assets/brand-tokens.css) como variables, sin crear un segundo tema competidor. Los tokens no implementan componentes ni cargan fuentes.

La versión 3 usa nombres de Figma: `--cs-fondo-pagina`, `--cs-texto-primario`, `--cs-fondo-acento`, etc. Los primitivos se nombran en español como en el archivo. Las variables tipográficas `--cs-type-…` incluyen familia, tamaño, peso e interlineado; aplicarlas a los estilos del proyecto y conservar el comportamiento responsive. No asignar tamaños de títulos desktop a mobile ni usar el ancho del frame como breakpoint sin revisar el layout.

## Migración desde la skill anterior

- Fondos: página gris #F3F3F3 y superficies blancas, en lugar de aplicar verde 50 a todo.
- Tipografía: Inter en lectura y títulos; Space Grotesk en UI y H4. No poner Seitu como preferencia de títulos web.
- Primario: lima con texto verde oscuro. Marca verde es otra variante, no el único botón principal.
- Semántica: alerta naranja, error rojo, emergencia azul, bordes y foco propios; no derivarlos todos del verde.
- Las escalas tienen nueva numeración. El verde de marca antes era `green.500` y ahora es `verde/700`; conservar por función, no por número. Los [tokens anteriores](legacy-web-tokens-2026-09-23.json) y [CSS anterior](legacy-web-tokens-2026-09-23.css) se preservan para comparar, no para importarlos junto al tema actual.
- Alias generales como `--cs-primary` apuntan ahora a la función documentada. Revisar cada uso antes de reemplazar una copia antigua. Ningún proyecto que ya copió la skill se actualiza automáticamente.

## Recursos y fuentes

Usar primero los logos, fotografías e iconos finales del proyecto y del Figma. Los SVG en `assets/logos/web/` son derivados históricos con geometría conservada: verdes #19542C y claros #F0F4F1. El sistema actual usa blanco en texto sobre marca y muestra logos negativos; no afirmar que los SVG claros históricos sean exportaciones exactas del Figma. Para reproducir una variante con bajada usar su original completo. Nunca reconstruir el logo escribiendo su nombre ni mezclar iconos inventados con la biblioteca entregada.

Un SVG externo en `img` no hereda `color` del padre. Si es necesario adaptar una variante, preservar sus trazados y registrar el color efectivo. La skill no incluye archivos de Inter ni Space Grotesk: usar archivos disponibles en el proyecto o fuentes oficiales autorizadas por el encargo; verificar que carguen realmente. Los fallbacks de sistema son propuestas técnicas, no fuentes aprobadas por Diseño.

## Comprobación al implementar

Comparar el componente y la pantalla correspondiente en desktop y mobile. Revisar tipografía realmente cargada, tamaño de logo, contrastes sobre fondos finales, estados hover/focus/error/disabled y uso con teclado/toque. Aplicar los comportamientos de menú, campos, alertas, diálogos, mapa y tablas recogidos en la referencia. No dar por cumplida WCAG porque la maqueta mencione la norma.

Conservar el footer final aprobado del proyecto y su componente compartido cuando exista. Los contactos, horarios, importes, fechas, categorías y textos de ejemplo del Figma requieren la fuente operativa del proyecto antes de publicarse.
