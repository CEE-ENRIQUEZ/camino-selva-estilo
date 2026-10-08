# Guía de marca de Camino Selva

> **Actualización web 2026-10-01:** consultar [Design System de Figma](figma-design-system.md). Para web esa fuente define ahora tipografía, componentes y tokens, además del color; las secciones de esta guía describen el anteproyecto y otros soportes.

## Procedencia y estado

Fuente: **Camino selva - Ajustes Anteproyecto**, Diseño Shakespear, septiembre de 2026, 15 páginas. Se conserva una copia idéntica en [camino-selva-anteproyecto-2026-09.pdf](camino-selva-anteproyecto-2026-09.pdf). Las páginas citadas aquí son posiciones físicas dentro del archivo, no la numeración impresa.

Este material es un anteproyecto. La revisión del usuario y la creación de esta skill no equivalen a una aprobación final de la marca. Si se aportan originales finales o un manual posterior, usarlos como fuente preferente y actualizar solo lo que haya cambiado.

**Actualización para web:** el usuario aportó el 23 de septiembre de 2026 una indicación del área de Diseño y la lámina `Frame 14 (1).pdf`. Para web y aplicaciones, [la paleta web](web-palette.md) prevalece sobre los colores del anteproyecto. La actualización de septiembre se limitaba al color digital; la posterior revisión de Figma amplía las reglas web y agrega Space Grotesk para interfaz.

La autoría del diseño pertenece a Diseño Shakespear. La copia local y los derivados mantienen esa procedencia; no asignarles una licencia abierta ni publicar el PDF como parte de una web por defecto.

## Lenguaje visual documentado

El símbolo combina un eje de camino con marcas centrales y trazos laterales que evocan vegetación. El logotipo usa mayúsculas y lettering propio. Las piezas reúnen masas de color, crema, fotografía de rutas y selva, y ampliaciones del símbolo.

Las páginas 9 a 12 muestran aplicaciones en vehículo, cartel de tarifas e Instagram. Sirven como referencias de composición y tono. Sus datos y escenas no acreditan operaciones, tarifas, condiciones de servicio ni cobertura geográfica concreta.

## Paleta del anteproyecto: referencia para otros soportes

**No usar esta tabla como paleta web.** La página 5 del anteproyecto muestra seis colores sin códigos oficiales. Los siguientes valores se extrajeron de sus componentes RGB y se redondearon a 8 bits. Se conservan como referencia visual histórica y para otros soportes según el encargo; no son equivalencias Pantone o CMYK aprobadas.

| Token | HEX derivado | RGB interno del PDF | Uso observado o interpretación |
|---|---|---|---|
| `forest` | `#005841` | 0.000, 0.347, 0.255 | Verde profundo dominante; logo y fondos |
| `cream` | `#FEFADF` | 0.997, 0.981, 0.874 | Fondo claro y marca en negativo |
| `lime` | `#97B400` | 0.591, 0.704, 0.000 | Acento verde vivo y superficies amplias |
| `orange` | `#F8803B` | 0.971, 0.502, 0.233 | Acento cálido y recurso gráfico |
| `terracotta` | `#BC3C16` | 0.738, 0.234, 0.088 | Superficie cálida y contraste territorial |
| `earth-red` | `#7E1B13` | 0.493, 0.107, 0.074 | Fondo oscuro cálido |

Los nombres de esta tabla son etiquetas históricas de la primera versión de la skill. Los tokens de implementación actuales usan la paleta web. Priorizar verde y crema en otros soportes es una interpretación de las aplicaciones del anteproyecto, no una proporción oficial de uso.

Crema sobre lima o naranja aparece en recursos gráficos. No extrapolar automáticamente esas combinaciones a texto pequeño, botones o información crítica. Evaluar su lectura en el soporte real y elegir una combinación de mayor contraste cuando corresponda.

## Tipografías documentadas

| Función | Familia | Página |
|---|---|---|
| Institucional | Seitu | 6 |
| Información vial | New Transport | 7 |
| Usos digitales | Inter | 8 |

El anteproyecto muestra muestras de pesos; no define tamaños, interlineados ni una escala tipográfica. Para web usar la escala explícita del Design System posterior. Seleccionar pesos y tamaños por legibilidad y jerarquía. La skill no incluye archivos OTF, TTF o WOFF ni los extrae de las fuentes incrustadas en el PDF. Emplear los archivos que ya tenga el proyecto o los que aporte el usuario.

Para un prototipo digital sin Seitu, Inter disponible en el proyecto puede servir como sustitución provisional. Si tampoco está Inter, utilizar una sans serif del sistema y dejar constancia de la sustitución. No declarar esa sustitución como tipografía institucional aprobada.

## Catálogo de recursos vectoriales

Los SVG conservan trazados del PDF, sin redibujar el símbolo ni convertir texto corriente en el logo. No son archivos maestros entregados por el estudio. Todas las variantes incluidas carecen de la bajada; no agregarla por composición improvisada si se requiere reproducir exactamente un lockup del documento.

| Archivo base en `assets/logos/` | Composición | Procedencia |
|---|---|---|
| `logo-stacked-green.svg` | Símbolo a la izquierda, nombre en dos líneas | Página 3 |
| `logo-horizontal-green.svg` | Símbolo a la izquierda, nombre en una línea | Página 4, fila inferior |
| `logo-vertical-green.svg` | Símbolo encima del nombre | Página 4, fila inferior |
| `symbol-green.svg` | Símbolo aislado | Página 3 |

Cada archivo tiene una variante `-cream.svg` con la misma geometría. El uso en crema sigue las inversiones de color de la página 5. Los SVG contienen solo trazados, tienen fondo transparente y no necesitan fuentes. Su atributo `viewBox` está ajustado al dibujo, sin área de protección incluida.

**Para web y aplicaciones utilizar `assets/logos/web/`.** Allí hay cuatro composiciones con sufijo `-green.svg` en `#19542C` y cuatro con sufijo `-light.svg` en `#F0F4F1`. Las formas y proporciones se conservan exactamente. Las variantes claras son una propuesta de implementación usando verde 50, no una nueva especificación del estudio. Evitan arrastrar el verde y el crema anteriores a la interfaz. Consultar `assets/asset-provenance.json` para conocer fuente, color y adaptación de cada recurso.

Los archivos usan `fill="currentColor"` y un atributo `color` con el color por defecto. Dentro de una etiqueta `img`, utilizar el archivo del color adecuado: el CSS del padre no cambia los trazados internos de un SVG externo. En SVG inline se puede controlar `color` explícitamente.

Respetar la relación ancho/alto y dejar espacio alrededor según la composición. El PDF no establece un mínimo de reproducción ni una unidad de protección: no inventar cifras como si fueran reglas oficiales. Los SVG extraídos se comprobaron visualmente contra el PDF; la extracción no certifica idoneidad para fabricación, bordado o corte.

La página 4 también muestra versiones con bajada en algunas composiciones. Si se necesita una de ellas, consultar el PDF y preferir el original vectorial específico del proyecto; no confundir las variantes incluidas con esas versiones.

## Mensajes y fotografía

- Nombre: **Camino Selva**.
- Descriptor: **Concesionario vial**.
- Mensaje recurrente: **Conectamos Misiones**.
- Otra frase presente: **Unimos caminos, atravesamos la selva.**

Usar estos mensajes cuando encajen en el contenido solicitado, sin añadir promesas de disponibilidad, emergencias o cobertura que no estén confirmadas. En fotografías, favorecer contexto territorial y caminos integrados al paisaje. Las imágenes de las maquetas del PDF no se incluyen como banco de fotos listo para publicación.

## Detalles del anteproyecto que no deben heredarse

- Página 2: las dos versiones no están rotuladas como anterior/propuesta. La skill utiliza la versión robusta presentada en la página 3 y en las aplicaciones posteriores; no atribuye aprobación final a esa selección.
- Página 4: la fila titulada "con bajada" incluye ejemplos sin descriptor. Guiarse por la composición visible.
- Página 12: aparece `primaveracasa` en las maquetas. No es una cuenta de Camino Selva confirmada.
- Páginas 13 y 14: numeración impresa 14 y 15. Citar las posiciones físicas del archivo.
- El cartel de la página 10 es una maqueta. No reutilizar sus importes y categorías como datos reales.

## Definiciones pendientes

El anteproyecto no especifica códigos finales de impresión, área de protección, tamaño mínimo ni composiciones completas para todos los soportes. El Design System posterior sí documenta iconos, espaciado, radios, efectos y componentes web: consultar esa fuente antes de proponerlos. Resolver lo restante según el proyecto. No utilizar los colores ni la firma roja de Diseño Shakespear como elementos de Camino Selva.
