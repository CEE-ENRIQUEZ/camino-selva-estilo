# Paleta web indicada por Diseño

> **Antecedente de septiembre:** para la implementación actual consultar [Design System de Figma](figma-design-system.md). Conserva los cuatro colores principales, cambia la numeración de escalas y agrega semántica, neutros y estados. Allí lima 700 queda definido como #7BA726; las observaciones de discrepancia de esta lámina se conservan como historial de su fuente. Los identificadores de las tablas siguientes no son los tokens de la versión 3.

## Fuente y precedencia

El usuario solicitó incorporar a la skill el criterio del área de Diseño: para web deben usarse los colores específicos de esta lámina, en lugar de los del manual de marca. La [captura del comentario](design-feedback-2026-09-23.png) conserva el contexto. Posteriormente aportó el archivo `Frame 14 (1).pdf`, guardado sin modificaciones como [fuente de color web](camino-selva-web-colors-2026-09-23.pdf). La fecha indica cuándo lo aportó el usuario, no una fecha de emisión del documento.

Esta paleta prevalece en web y aplicaciones sobre la tabla de RGB extraídos del anteproyecto. El anteproyecto sigue siendo referencia para geometría del logo, tipografías, mensajes y otros soportes. No extender esta actualización a impresión por defecto.

Se contrastaron los HEX impresos con los rellenos vectoriales del PDF; no se muestrearon píxeles de una captura de pantalla. La procedencia y las discrepancias están registradas en `assets/web-color-provenance.json`.

## Colores principales

| Función | Token | HEX | Evidencia |
|---|---|---|---|
| Verde primario | `green.500` | `#19542C` | Rótulo BASE verde, escala y relleno de la primera muestra superior |
| Lima secundario | `lime.500` | `#B7E768` | Escala y relleno de la segunda muestra superior |
| Bronce terciario | `bronze.500` | `#E5B25D` | Escala y relleno de la tercera muestra superior |
| Naranja, acento adicional | `orange` | `#F6511D` | Relleno vectorial de la cuarta muestra superior; su etiqueta es incorrecta |

Los nombres de tokens en inglés son identificadores de implementación. La lámina no define una escala de naranja ni le asigna un estado funcional.

## Escalas para implementación

| Nivel | Verde | Lima | Bronce |
|---|---|---|---|
| 50 | `#F0F4F1` | `#F9FCEE` | `#FEFBF3` |
| 100 | `#D9E8DD` | `#F0F9D0` | `#FBF3E0` |
| 200 | `#B3D1BC` | `#E3F3A1` | `#F7E5BA` |
| 300 | `#7FBBA6` | `#D4ED72` | `#F2D691` |
| 400 | `#4BA590` | `#C3E743` | `#EDC568` |
| 500 | `#19542C` | `#B7E768` | `#E5B25D` |
| 600 | `#0E4922` | `#9ACC34` | `#D89939` |
| 700 | `#0A381A` | `#7BA726` * | `#C17E28` |
| 800 | `#053012` | `#5F8A1F` | `#A86620` |
| 900 | `#021009` | `#2D3F0A` | `#4A2F0F` |

Todos los valores de las escalas coinciden entre etiqueta y relleno salvo el marcado con asterisco. No recalcular los tonos para hacerlos más regulares: por ejemplo, lima 400 y 500 son los valores indicados por Diseño.

## Discrepancias de la lámina y criterio aplicado

1. **Fila superior:** las cuatro etiquetas repiten verde 50, 100, 200 y 300, pero las muestras son los cuatro colores principales. Para esa fila se toman los rellenos vectoriales: verde `#19542C`, lima `#B7E768`, bronce `#E5B25D` y naranja `#F6511D`. Las tres primeras se corroboran con el nivel 500 de sus escalas.
2. **BASE de lima y bronce:** ambos repiten `#19542C`, el verde primario. No usar ese texto para sustituir sus escalas; sus tonos 500 y las muestras superiores coinciden entre sí.
3. **Lima 700:** la etiqueta indica `#7BA726`, mientras que el relleno es `#5F8A1F`, igual que lima 800. En septiembre se eligió provisionalmente el HEX escrito y se conservó la discrepancia en la procedencia. El Design System inspeccionado posteriormente define `lima/700` como `#7BA726`; ese es el valor de implementación actual, sin afirmar que etiqueta y relleno de esta lámina antigua coincidían.

## Alias propuestos en septiembre, reemplazados por el Design System

Los alias de la versión anterior eran propuestas: superficie = verde 50, texto = verde 900, acción principal = verde 500, texto sobre acción principal = verde 50, acento secundario = lima 500 y acento terciario = bronce 500. Se conservan en los archivos legacy; no aplicarlos a una interfaz nueva. El Design System posterior sí define colores por función, incluyendo error, alerta, bordes y foco.

Para fondos oscuros, los SVG web claros utilizan verde 50 como adaptación propuesta de las versiones negativas del logo. Los trazados permanecen iguales; solo cambia el color.
