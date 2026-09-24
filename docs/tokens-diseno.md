# Tokens de diseño - Plastic Bags SAS

## 1. Lectura visual del brochure

La identidad actual combina:

- Verdes salvia y bosque.
- Fondos tipo papel en tonos gris verdoso y marfil.
- Verde hoja como acento.
- Tipografía serif editorial para títulos.
- Tipografía sans serif geométrica para textos y datos.
- Fotografías orgánicas y texturas naturales.
- Bloques rectangulares amplios, con pocos bordes redondeados.

Las fuentes incrustadas en el PDF son **Quiche Display** y **Montserrat**. Quiche Display aporta el gesto editorial; Montserrat sostiene la información funcional.

## 2. Paleta extraída del brochure

Los valores se obtuvieron de los fondos, bloques y elementos predominantes del PDF renderizado. Al existir texturas y transparencias, son aproximaciones normalizadas para uso digital.

| Token de origen | Color | Uso observado |
| --- | --- | --- |
| Pino | `#34493C` | Logo, texto oscuro y detalles |
| Bosque | `#4E654E` | Bloques oscuros |
| Salvia | `#68826B` | Fondos principales |
| Salvia clara | `#96AA94` | Fondos de categorías |
| Niebla | `#B7C4BA` | Fondos claros y textura |
| Papel | `#EAEAE6` | Superficies claras |
| Hoja | `#90AE74` | Hojas del logo y acentos |
| Blanco suave | `#F7F9F7` | Texto invertido y fondos |

## 3. Paleta digital recomendada

La paleta web conserva el carácter del brochure, pero separa con claridad los colores decorativos de los colores que deben sostener texto.

### Marca y superficies

| Token | Valor | Uso recomendado |
| --- | --- | --- |
| `brand-950` | `#173D2B` | Texto de marca, CTA oscuro y footer |
| `brand-900` | `#234A35` | Hover de CTA y bloques de alto contraste |
| `brand-800` | `#34493C` | Superficie oscura principal |
| `brand-700` | `#4E654E` | Superficie secundaria oscura |
| `brand-600` | `#68826B` | Decoración, fondos de texto grande |
| `brand-400` | `#96AA94` | Fondos suaves y elementos gráficos |
| `brand-200` | `#B7C4BA` | Líneas, bordes y superficies suaves |
| `brand-100` | `#DDE6DF` | Fondos alternos |
| `brand-50` | `#F2F6F3` | Fondo verde casi blanco |

### Acento hoja

| Token | Valor | Uso recomendado |
| --- | --- | --- |
| `leaf-700` | `#5F7D42` | Iconos y texto de acento sobre fondos claros |
| `leaf-500` | `#90AE74` | Elementos gráficos |
| `leaf-400` | `#A3C27E` | CTA luminoso sobre fondos oscuros |
| `leaf-200` | `#D9E8C5` | Etiquetas y fondos destacados |

### Neutros cálidos

| Token | Valor | Uso recomendado |
| --- | --- | --- |
| `ink-950` | `#172019` | Texto principal |
| `ink-700` | `#405047` | Texto secundario |
| `paper-100` | `#EAEAE6` | Secciones editoriales |
| `paper-50` | `#F4F1E8` | Fondo cálido principal |
| `white` | `#FFFFFF` | Superficies y texto invertido |

### Asignación semántica

- Fondo general: `paper-50`.
- Fondo alterno: `brand-50`.
- Fondo oscuro: `brand-800`.
- Texto principal: `ink-950`.
- Texto secundario: `ink-700`.
- Texto sobre fondos oscuros: `white` o `brand-50`.
- CTA principal: fondo `leaf-400`, texto `brand-950`.
- CTA secundario: transparente, borde y texto `brand-800`.
- Enlaces: `brand-900`; estado hover `leaf-700`.
- Bordes: `brand-200` con opacidad moderada.

## 4. Contraste comprobado

Combinaciones recomendadas para texto normal:

| Texto | Fondo | Relación aproximada |
| --- | --- | ---: |
| `#FFFFFF` | `#34493C` | 9.70:1 |
| `#F7F9F7` | `#4E654E` | 6.02:1 |
| `#173D2B` | `#A3C27E` | 6.08:1 |
| `#1B2C22` | `#EAEAE6` | 12.18:1 |
| `#1B2C22` | `#F4F1E8` | 13.00:1 |

Evitar texto blanco pequeño sobre `brand-600` (`#68826B`): su contraste aproximado es 4.21:1. Puede usarse para títulos grandes o como color decorativo, pero el texto normal necesita una superficie más oscura.

## 5. Tipografía

### Tipografías encontradas en el PDF

- Display: Quiche Display Regular, Medium y Bold.
- Sans serif: Montserrat Regular, Medium y Bold.

### Combinación web recomendada

**Titulares: Fraunces**

- Conserva la personalidad orgánica y editorial de Quiche Display.
- Funciona bien en títulos grandes y permite ajustar peso y contraste.
- Usar pesos 500, 600 y 700.

**Texto e interfaz: Manrope**

- Tiene una lectura más abierta en pantalla que Montserrat.
- Funciona bien en párrafos, navegación, botones, fichas y cifras.
- Usar pesos 400, 500, 600 y 700.

### Alternativa continuista

- Quiche Display para títulos, si la empresa cuenta con licencia web.
- Montserrat para cuerpo e interfaz.

### Alternativa de alta disponibilidad

- DM Serif Display para títulos.
- Inter para cuerpo e interfaz.

### Reglas tipográficas

- Títulos con serif; textos, botones y navegación con sans serif.
- Evitar párrafos largos centrados. Reservar el centrado para títulos y mensajes breves.
- Mantener párrafos entre 55 y 70 caracteres por línea.
- Usar mayúsculas sostenidas solo en etiquetas cortas.
- Usar pesos 600 o 700 para botones; no depender únicamente del color.

## 6. Escala tipográfica fluida

| Token | Tamaño sugerido | Uso |
| --- | --- | --- |
| `display-xl` | `clamp(3.5rem, 8vw, 7rem)` | Mensaje editorial excepcional |
| `display-lg` | `clamp(2.75rem, 6vw, 5.5rem)` | H1 del hero |
| `heading-1` | `clamp(2.25rem, 4.5vw, 4rem)` | Títulos de sección principales |
| `heading-2` | `clamp(1.75rem, 3vw, 2.75rem)` | Subsecciones |
| `heading-3` | `clamp(1.25rem, 2vw, 1.75rem)` | Tarjetas |
| `body-lg` | `clamp(1.0625rem, 1.5vw, 1.25rem)` | Entradillas |
| `body-md` | `1rem` | Texto base |
| `body-sm` | `0.875rem` | Metadatos y notas |
| `label` | `0.75rem` | Etiquetas breves |

Interlineados:

- Display y títulos: `0.95` a `1.1`.
- Texto grande: `1.5`.
- Texto base: `1.65`.
- Etiquetas y botones: `1.2`.

## 7. Espaciado

Usar una base de 4 px con saltos más amplios para mantener el aire editorial.

| Token | Valor |
| --- | ---: |
| `space-1` | `0.25rem` |
| `space-2` | `0.5rem` |
| `space-3` | `0.75rem` |
| `space-4` | `1rem` |
| `space-6` | `1.5rem` |
| `space-8` | `2rem` |
| `space-12` | `3rem` |
| `space-16` | `4rem` |
| `space-24` | `6rem` |
| `space-32` | `8rem` |

- Separación vertical de secciones: `clamp(4.5rem, 10vw, 8rem)`.
- Ancho máximo de contenido: `75rem`.
- Ancho de lectura: `42rem`.
- Margen lateral: `clamp(1.25rem, 4vw, 4rem)`.

## 8. Forma, bordes y profundidad

El brochure usa geometría sobria. La landing debería conservarla y evitar tarjetas excesivamente redondeadas.

- Radio pequeño: `0.375rem`.
- Radio medio: `0.75rem`.
- Radio grande: `1.25rem`, reservado para fotografías o módulos destacados.
- Botones: radio `0.5rem` o estilo cápsula solo si los referentes lo justifican.
- Borde: `1px solid rgba(52, 73, 60, 0.18)`.
- Sombra suave: `0 12px 32px rgba(23, 61, 43, 0.10)`.
- Sombra elevada: `0 20px 60px rgba(23, 61, 43, 0.16)`.

La textura de papel puede aplicarse como una capa muy sutil con opacidad entre 3% y 6%, sin reducir la legibilidad ni competir con las fotos de producto.

## 9. Imágenes e iconografía

- Producto recortado sobre superficies limpias para explicar categorías.
- Fotografía contextual para introducir hogar, mascotas y sostenibilidad.
- Iconos lineales con esquinas suaves y grosor consistente de 1.5 a 2 px.
- Iconos en `brand-800` o `leaf-700` sobre fondos claros.
- Evitar mezclar fotografías de bancos con estilos de iluminación incompatibles.
- Mantener proporciones repetibles: `4:3` para tarjetas, `3:2` para secciones y `1:1` para detalles de producto.

## 10. Movimiento

- Duración rápida: `160ms`.
- Duración normal: `240ms`.
- Duración de entrada: `480ms`.
- Curva: `cubic-bezier(0.22, 1, 0.36, 1)`.
- Desplazamientos discretos de 8 a 16 px.
- Respetar `prefers-reduced-motion`.

Las animaciones deben ayudar a revelar categorías o atributos. No deben dificultar la lectura ni bloquear la navegación.

