# Design System web de Camino Selva

## Fuente y alcance de la revisión

Inspección directa con el complemento de Chrome el **1 de octubre de 2026**, en el archivo [Sitio web Camino Selva](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva). El usuario indicó que este archivo define cómo debe verse la página. Se leyó la página **Design System**, sus fundamentos y descripciones de componentes; se contrastaron el home desktop con hover, el hero mobile y las notas de entrega de la página **Sitio web mobile · WCAG 2.2 AA**. No se modificó el archivo Figma ni se ejecutaron los flujos de una web implementada.

La copia [Fundamentos](figma-fundamentos-2026-10-01.pdf) se exportó desde la interfaz de Figma. Es una captura documental de una página muy alta, no el archivo completo ni una versión oficial fechada por Diseño. Los valores de componentes que no aparecen en ese PDF provienen del inspector y sus descripciones, con enlaces abajo. No se exportó la biblioteca entera de iconos, fotos o fuentes.

## Precedencia y convivencia de versiones

Para nuevas implementaciones web, los tokens y componentes de **Design System** prevalecen sobre las propuestas de la skill y la lámina web anterior. Las maquetas de páginas conservan la referencia de composición y contenido. En el mismo archivo conviven versiones: el home desktop con hover aún muestra la navegación sobre la foto y el rótulo «Usuarios»; el componente Header prescribe una barra blanca al 85 % y «Atención al usuario». No copiar automáticamente las reglas anteriores cuando contradigan el componente actualizado.

La numeración de primitivos cambió: `verde/700` es `#19542C`, `verde/500` ahora es `#315743`; `lima/400` es `#B7E768`. Por eso no sustituir tokens antiguos por número ni mezclar escalas de ambas fuentes. Lima 700 queda documentado como `#7BA726`, resolviendo para este sistema la duda de la lámina anterior.

Si un proyecto ya tiene una composición explícitamente aprobada por el usuario —por ejemplo el footer final del home—, conservar esa decisión y reutilizar su componente compartido. Esta revisión de la skill no autoriza por sí sola reemplazar diseños de otros proyectos.

## Colores por función

| Uso | Token de Figma | HEX |
|---|---|---|
| Fondo de página | fondo/pagina | #F3F3F3 |
| Tarjetas y superficies | fondo/superficie | #FFFFFF |
| Marca | fondo/marca | #19542C |
| Marca intensa | fondo/marca-fuerte | #0E4922 |
| Acción primaria / acento | fondo/acento | #B7E768 |
| Acento suave / hover de contorno | fondo/acento-suave | #E3F3A1 |
| Texto principal | texto/primario | #1C2620 |
| Texto secundario | texto/secundario | #5F6A63 |
| Texto placeholder | texto/placeholder | #6B756E |
| Texto sobre marca | texto/sobre-marca | #FFFFFF |
| Texto sobre lima | texto/sobre-acento | #0E4922 |
| Destacado sobre marca | texto/destacado-sobre-marca | #E5B25D |
| Emergencia | fondo/emergencia | #074170 |
| Reportar / alerta | fondo/alerta | #F6511D |
| Error | texto/error | #B3261E |
| Fondo de error | fondo/error-suave | #FBEAE8 |
| Pie oscuro | fondo/oscuro | #333333 |
| Pie oscuro intenso | fondo/oscuro-fuerte | #242424 |

La lista completa de primitivos y referencias semánticas está en [brand-tokens.json](../assets/brand-tokens.json). No reducir el sistema a cuatro colores ni sustituir el azul del gráfico 140 por un azul aproximado: usar el recurso original de la variante elegida.

### Discrepancia sobre naranja

En Fundamentos, `texto/sobre-marca` aparece dos veces: blanco para el verde y negro `neutro/1000` para naranja. La muestra naranja exportada muestra texto blanco aunque la etiqueta indica negro. El botón Alerta inspeccionado muestra texto oscuro. La skill mantiene `texto/sobre-marca` blanco y crea **como decisión de implementación** `texto/sobre-alerta` negro, sin atribuir este nuevo nombre a Figma. No unificar ambos ni trasladar el blanco de la muestra a textos pequeños sobre naranja. La discrepancia de nombres/muestra queda pendiente de corrección en el documento de Diseño.

## Tipografías

Inter para títulos y párrafos; Space Grotesk para navegación, botones, rótulos y datos. Excepción explícita: H4 también usa Space Grotesk. Seitu y New Transport siguen como referencias para otros soportes, no como sustitutos del sistema web.

| Estilo | Familia / peso | Tamaño px | Interlineado |
|---|---|---:|---:|
| Display/XL | Inter / 800 | 96 | 1.1 |
| Título/H1 | Inter / 800 | 64 | 1.15 |
| Título/H2 | Inter / 800 | 48 | 1.2 |
| Título/H3 | Inter / 700 | 32 | 1.25 |
| Título/H4 | Space Grotesk / 700 | 24 | 1.4 |
| Título/H5 | Inter / 700 | 20 | 1.5 |
| Texto/Lead | Inter / 400 | 24 | 1.5 |
| Texto/Cuerpo L | Inter / 400 | 20 | 1.5 |
| Texto/Cuerpo M | Inter / 400 | 16 | 1.5 |
| Texto/Cuerpo M Bold | Inter / 700 | 16 | 1.5 |
| Texto/Nota | Inter / 400 | 14 | 1.5 |
| Texto/Legal | Space Grotesk / 400 | 12 | 1.5 |
| UI/Nav | Space Grotesk / 500 | 16 | 1.5 |
| UI/Botón | Space Grotesk / 700 | 16 | 1.2 |
| UI/Eyebrow | Space Grotesk / 700 | 14 | 1.5 |
| UI/Label | Space Grotesk / 400 | 14 | 1.5 |
| UI/Dato | Space Grotesk / 700 | 40 | 1.2 |
| Mobile/Display | Inter / 800 | 48 | 1.1 |
| Mobile/H1 | Inter / 800 | 40 | 1.15 |
| Mobile/H2 | Inter / 800 | 32 | 1.2 |
| Texto/Cuerpo L Bold | Inter / 700 | 20 | 1.5 |
| UI/Cuerpo | Space Grotesk / 400 | 16 | 1.5 |
| UI/Link sección | Space Grotesk / 500 | 16 | 1.5 |
| UI/Chip | Space Grotesk / 700 | 14 | 1.2 |
| UI/Número destacado | Space Grotesk / 700 | 28 | 1 |

El JSON conserva interlineados como multiplicadores, no redondeos del rótulo. Cuerpo M: separación entre párrafos 36 px; Cuerpo L: 45 px; Lead: 54 px. Botón y Eyebrow en mayúsculas; enlaces de sección como «VER MÁS» en mayúsculas. El rótulo de Cuerpo L Bold solo imprime interlineado; su separación de 45 px en los tokens reutiliza la regla general de Cuerpo L. No justificar párrafos. La documentación marca 14 px como mínimo general y 12 px para Legal. La skill no contiene archivos de fuentes; comprobar carga y pesos reales en cada proyecto.

## Medidas y efectos

- Espaciado: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80 y 120 px.
- Radios: 0; sm 4; md 10; lg 16; xl 24; pill 999 px. Los contenedores del catálogo no son necesariamente el tamaño de un componente: inspeccionar la variante o instancia.
- Botones: mínimo 44 px de alto. Primario y Marca Default inspeccionados: padding 12 px vertical y 24 px horizontal, gap 8 px, radio md. No imponer el ancho de muestra 138 px a todo texto.
- Foco: contorno de 3 px, separación 2 px; verde oscuro sobre claro y lima sobre oscuro. Conservar el foco visible también en cabeceras fijas.
- Elevación 2 observada en Modal y Card estación: `0 8px 24px 0 rgb(28 38 33 / 14%)`. La documentación menciona Elevación 1 para cards, pero esta revisión no extrajo sus parámetros; no inventarlos como oficiales.
- Frames inspeccionados: home desktop hover 1440 × 1024; home mobile 390 px de ancho. Son tamaños de referencia, no una especificación de breakpoints CSS ni alturas fijas obligatorias.

## Componentes e interacción documentada

| Componente | Reglas observadas | Fuente |
|---|---|---|
| Button | Primario lima, Marca verde, Contorno, Contorno inverso, Alerta naranja. Estados Default, Hover, Foco y Deshabilitado. UI/Botón, una acción primaria por página; explicar acciones no disponibles. | [570-1242](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=570-1242) |
| Link | Subrayado en enlaces de contenido, incluidos teléfono/correo. Enlace de sección «VER MÁS» con nombre accesible contextual. Navegación principal tiene su indicador propio. | [570-1257](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=570-1257) |
| 140 / TelePASE | Usar gráficos originales y sus variantes compacta, mediana y completa. 140 lleva enlace tel:140 y nombre accesible; el gráfico interno puede ser decorativo. Identificar TelePASE como enlace externo si abre otra ventana. | [140: 570-1319](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=570-1319) |
| Header | Logo fuera de la barra desktop; barra redondeada con navegación, contacto, 140 y TelePASE. Sobre imagen: blanco 85 % con desenfoque; variante clara en internas. Mobile compacto con logo, 140 y botón menú. | [576-295](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=576-295) |
| Nav item | Página actual con línea inferior 3 px y aria-current; disparador de submenú como button con aria-expanded. La navegación debe funcionar con teclado y toque, además del hover mostrado en desktop. | Documentación visible en Design System |
| Menú mobile | Fondo verde, texto blanco, acentos lima; Inicio, Tarifas y servicios, Atención al usuario, Nosotros, Preguntas frecuentes, Trabajá con nosotros. Ítems de 44 px. Cerrar con Esc o botón rotulado y devolver foco al disparador. Si se implementa como superposición modal, contener el foco mientras está abierta. | [577-1044](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=577-1044) |
| Footer | Columnas con títulos lima subrayados; variantes mobile en acordeón, 140 y TelePASE completos. Barra de actualización neutro/600; redes con nombre accesible. Reutilizar el footer final ya aprobado del proyecto cuando exista. | [577-1043](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=577-1043) |
| Text field | Etiqueta siempre visible, placeholder separado, línea inferior fuerte; error con borde, icono y mensaje, aria-describedby y aria-invalid; autocomplete según el dato. Línea de foco 3 px. | [570-2014](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=570-2014) |
| Opción radio | Input nativo y label que abarca la tarjeta; fieldset/legend, flechas de teclado; selección con borde 2 px y punto, foco 3 px. | [573-67](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=573-67) |
| Alerta | Error: resumen y enlaces a campos, role=alert. Información: role=status. Icono y texto además del color. | [574-59](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=574-59) |
| Modal | Título y paso actual, role=dialog, aria-modal, foco contenido, Esc/cierre y restauración de foco. Pantalla completa en mobile. Desktop de referencia 800 px, radio 24 y elevación 2. | [574-60](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=574-60) |
| Card estación | Mapa operable con mouse y teclado, foco al detalle, alternativa en lista de estaciones; servicios con icono y texto. Card de referencia 420 px, padding 24, gap 16, radio 16, elevación 2. | [570-1776](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=570-1776) |

Los menús desktop conservan panel claro con encabezado y grupos de enlaces verdes. El [home con hover](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=147-120) inspeccionado muestra «Tarifas» y «Servicios» en dos columnas, mientras la captura anterior tenía tres. Los [tres PDFs de menús y su estructura](desktop-menus.md) también están incorporados: Tarifas MVP usa dos columnas; Atención y Nosotros, tres. Elegir la composición del frame vigente de la página que se implemente; no fijar tres columnas como una norma universal. Los bordes azules/morados, medidas y comentarios del editor no pertenecen al diseño.

La biblioteca también contiene iconos de servicios, valores, redes y logos con bajada. Preferir esos originales disponibles en el proyecto/Figma. Los SVG históricos incluidos en la skill no equivalen al catálogo completo ni sustituyen un lockup final con descriptor.

## Mobile y notas de entrega

El [hero mobile](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=595-4022) tiene foto con velo negro; el inspector muestra un gradiente con opacidades 60 %, 50 % y 80 %. No se extrajeron posiciones ni ángulo: conservar el recurso/instancia o verificarlos antes de reproducir el gradiente exacto.

Las [notas de handoff](https://www.figma.com/design/o6gDmCfcxPq2gyouEvOHQ3/Sitio-web-Camino-Selva?node-id=598-7654) piden cuadro tarifario como tabla HTML, lectura sin desplazamiento horizontal de página a 390 px, carruseles con controles, aviso de ruta con pausa y sin marquesina en mobile, orden de lectura coherente, alternativa de mapa en lista y textos alternativos. Mantener esos comportamientos al implementar, sin copiar datos operativos de ejemplo.

Los ratios y las menciones WCAG del archivo son documentación de Diseño. Esta inspección no verificó la auditoría de «322 textos» declarada allí ni certifica la web: contrastes sobre fotos/transparencias, teclado, reflow, carga de fuentes y estados deben comprobarse en la implementación real.
