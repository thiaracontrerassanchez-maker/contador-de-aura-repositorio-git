# Contador de Aura — Expo Técnica

Implementación (de ejemplo) del proyecto **"Contador de Aura"** (Introducción a la Programación,
4ºB IPP).
Programa interactivo en Python: una persona se para frente a la cámara, se mueve
durante un tiempo determinado, y el sistema convierte ese movimiento (y algunos
movimientos especiales reconocidos, como el **dab**, el **sigma** o el **67**) en un
puntaje de "Aura", mostrando un resultado final con una categoría.

## Tecnologías usadas 

| Herramienta | Para qué se usa en este proyecto |
|---|---|
| **Python** | Lenguaje principal de todo el programa |
| **OpenCV** | Acceso a la cámara, captura de video y detección de movimiento (diferencia entre frames) |
| **MediaPipe** | Detección de la postura corporal (hombros, codos, muñecas, etc.) para reconocer movimientos especiales |
| **Pygame** | Reproducción de sonidos y música de fondo (generados por código, sin archivos externos) |
| **Tkinter** | Interfaz gráfica: video en vivo, puntaje, cuenta regresiva, botones y pantalla de resultado |
| **NumPy** | Procesamiento de las imágenes de la cámara y generación de las ondas de sonido |

## Estructura del proyecto

```
contador_de_aura/
├── main.py                  # Punto de entrada (ejecutar este archivo)
├── requirements.txt
├── README.md
└── src/
    ├── config.py             # Todas las constantes ajustables del proyecto
    ├── video_source.py       # Manejo de la cámara (con modo demo si no hay cámara)
    ├── motion_detector.py    # Detección de movimiento con OpenCV
    ├── pose_detector.py      # Detección de poses/movimientos especiales con MediaPipe
    ├── scoring.py            # Sistema de puntaje y categorías de aura
    ├── audio_manager.py      # Sonidos y música generados con NumPy + Pygame
    └── ui.py                 # Interfaz gráfica con Tkinter

# assets/models/ se crea solo (no viene en el proyecto): ahí se guarda el
# modelo de MediaPipe la primera vez que se descarga.

**`main.py`** es el punto de entrada: el archivo que se ejecuta con `python main.py`. No tiene lógica propia, solo arma las piezas: crea la cámara, los detectores, el audio y la ventana, y se encarga de cerrar todo prolijamente (liberar la cámara, etc.) cuando se cierra el programa.

**`requirements.txt`** lista las librerías necesarias (OpenCV, MediaPipe, pygame-ce, NumPy, Pillow) con comentarios explicando por qué se eligió cada versión, incluidos los dos problemas de instalación que ya tuve en mi notebook.

**`README.md`** es la documentación pública del repositorio: qué es el proyecto, cómo instalarlo y ejecutarlo, y cómo se juega. Es lo primero que ve cualquiera que entre al repo en GitHub.

**`src/`** es la carpeta donde vive toda la lógica del programa, dividida en un archivo por responsabilidad:

- **`__init__.py`**: archivo vacío (solo con un comentario) que le dice a Python que `src` es un paquete importable. No hace nada por sí mismo.
- **`config.py`**: todas las constantes ajustables del proyecto en un solo lugar (duración de la prueba, sensibilidad del movimiento, puntos de cada categoría de aura, colores de la interfaz, volumen, etc.), para poder "calibrar" el programa sin tocar la lógica de los demás archivos.
- **`video_source.py`**: abre la cámara con OpenCV. Si no encuentra ninguna, entra en un "modo demo" que genera una imagen animada simulada (un círculo moviéndose), para poder probar el resto del programa sin depender de tener una cámara conectada.
- **`motion_detector.py`**: calcula cuánto movimiento hay entre un frame de cámara y el siguiente (escala de grises, desenfoque, diferencia de píxeles, umbral). No sabe nada de puntajes ni de interfaz, solo devuelve un número.
- **`pose_detector.py`**: usa MediaPipe para detectar la postura del cuerpo (hombros, codos, muñecas) y, a partir de ángulos entre esos puntos, reconoce los movimientos especiales (dab, sigma, "67"). También se encarga de descargar solo el archivo de modelo de MediaPipe la primera vez que hace falta.
- **`scoring.py`**: el sistema de puntaje. Convierte el movimiento detectado en puntos de aura acumulados, suma los puntos extra por movimientos especiales, y decide la categoría final ("Aura Baja", "AURA INFINITA", etc.) según los umbrales de `config.py`. Es el módulo más simple y no depende de OpenCV, MediaPipe ni Tkinter.
- **`audio_manager.py`**: genera los sonidos del juego (efectos y música de fondo) como ondas creadas con NumPy y los reproduce con Pygame, sin necesitar archivos de audio externos.
- **`ui.py`**: la interfaz gráfica en Tkinter. Dibuja la ventana, el video en vivo, el puntaje, la cuenta regresiva, los botones y la pantalla de resultado, y maneja la máquina de estados (IDLE → COUNTDOWN → RUNNING → RESULT) que conecta todos los módulos anteriores.

Una carpeta `assets/models/` se crea sola la primera vez que se ejecuta el programa (ahí se guarda el modelo de MediaPipe descargado); por eso no está en el repositorio ni se sube a GitHub.

```

## Instalación

Se recomienda usar un entorno virtual:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt
```

> **Nota:** MediaPipe no siempre tiene soporte inmediato para las versiones de
> Python más nuevas apenas salen. Si falla la instalación, probar con una
> versión de Python un poco más antigua (por ejemplo, 3.11 o 3.12).

### Problemas comunes al instalar en Windows (Por experiencia propia)

**Error al instalar `pygame` ("Failed to build 'pygame'", pide Visual Studio,
`ModuleNotFoundError: No module named 'distutils.msvccompiler'`, etc.):**
esto pasa cuando la versión de Python instalada es muy nueva (por ejemplo,
recién salida) y todavía no existe un instalador ya compilado ("wheel") de
`pygame` para esa versión en Windows; entonces `pip` intenta compilarlo desde
cero y necesita herramientas de compilación de Visual Studio que la mayoría
no tiene instaladas. Por eso este proyecto usa **`pygame-ce`** (Pygame
Community Edition) en vez de `pygame` clásico: es un fork mantenido por los
mismos desarrolladores, tiene instaladores listos para versiones de Python
mucho más nuevas, y en el código no cambia nada (se sigue escribiendo
`import pygame`). Si el error persiste:

1. Verificar la versión de Python instalada: `python --version`.
2. Si es una versión muy nueva (3.13, 3.14 o más), instalar Python 3.12
   desde [python.org](https://www.python.org/downloads/) y crear el entorno
   virtual con esa versión en vez de la más nueva.
3. Volver a correr `pip install -r requirements.txt`.

## Ejecución

```bash
python main.py
```

- Si la computadora tiene cámara, se abre la ventana mostrando la imagen en vivo.
- Si **no** hay cámara conectada, el programa avisa por consola y arranca en
  "modo demostración" (una imagen animada simulada), para poder probar toda la
  interfaz, el puntaje y el audio igual.
- La **primera vez** que se ejecuta el programa con MediaPipe instalado, se
  descarga automáticamente un archivo de modelo (~5 MB) necesario para
  detectar la postura corporal; hace falta conexión a internet solo en ese
  momento. Las siguientes veces ya no vuelve a descargarlo (queda guardado en
  `assets/models/`). Conviene ejecutar el programa una vez con internet
  *antes* del día de la Expo Técnica, para que el modelo ya esté descargado.
- Si **MediaPipe** no está instalado, falla al cargar, o no se pudo descargar
  el modelo (por ejemplo, sin conexión a internet), el programa sigue
  funcionando igual: el puntaje por movimiento general funciona normalmente,
  solo se desactivan los puntos extra por dab/sigma/67.

## Cómo se juega

1. Presionar **Iniciar**.
2. Cuenta regresiva de 3 segundos para prepararse.
3. Durante 20 segundos (configurable), moverse frente a la cámara: cuanto más
   movimiento, más puntos de Aura. Reconocer un **dab**, un **sigma** o el
   gesto de **"67"** (mover las manos alternadamente arriba y abajo) da puntos
   extra de golpe (Pueden agregar más según lo consideren).
4. Al terminar el tiempo, se muestra el puntaje final y la categoría de Aura
   obtenida (Aura Negativa, Baja, Media, Alta, Legendaria o AURA INFINITA) también pueden cambiar las categorías como les parezca mejor, son solo ejemplos.
5. Presionar **Reiniciar** para que participe otra persona.

## Ajustar el comportamiento

Todos los valores que conviene "calibrar" el día de la Expo (duración de la
prueba, sensibilidad del movimiento, puntos de cada categoría, umbrales de las
poses especiales, colores, volumen) están reunidos en `src/config.py`, con
comentarios explicando cada uno.

## Limitaciones y posibles mejoras (para seguir investigando)

- El reconocimiento de "dab", "sigma" y "67" usa reglas simples basadas en
  ángulos y posiciones del cuerpo (no un modelo entrenado específicamente para
  esas poses), tal como plantea el informe como punto a investigar. Los
  umbrales en `config.py` pueden ajustarse si no detectan bien con distintas
  personas o cámaras.
- La calidad de la detección de movimiento depende de la iluminación del
  espacio y de que la cámara enfoque bien a la persona, como se menciona en la
  sección "Recursos de hardware" del informe.
- Se podrían agregar más movimientos especiales siguiendo el mismo patrón que
  ya usan `_es_dab`, `_es_sigma` y `_es_gesto_67` en `src/pose_detector.py`.
