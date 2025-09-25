# Control de Motor a Pasos M35SP-7T con Raspberry Pi Pico W y L9110S

Este proyecto implementa el control de un **motor a pasos M35SP-7T** utilizando un **puente H L9110S** y una **Raspberry Pi Pico W** actuando como servidor web.  
El sistema permite manejar el motor desde una **interfaz gráfica en un navegador**, mostrando en tiempo real la cantidad de pasos y la posición angular del motor en un **reloj digital**.

---

## Características principales

- Motor a pasos **M35SP-7T** (7.5° por paso → 48 pasos por vuelta).  
- Control mediante **puente H L9110S**.  
- Servidor web alojado en la **Raspberry Pi Pico W**.  
- Interfaz con botones:
  - `Clockwise (CW)` → sentido horario.  
  - `Counter Clockwise (CCW)` → sentido antihorario.  
  - `Start` → avanza el motor una cantidad de pasos predefinida.  
- Visualización en tiempo real:
  - **Número de pasos actuales**.  
  - **Reloj gráfico** con marcas cada 10° y aguja que indica la posición angular.  

---

## Materiales

- Raspberry Pi Pico W  
- Motor a pasos **M35SP-7T (7.5°/paso, 48 pasos por vuelta)**  
- Módulo controlador **L9110S**  
- Protoboard y cables de conexión  
- Fuente de alimentación de 5V  
- Computadora para programar y ejecutar el servidor web  

---

## Conexiones

```plaintext
Raspberry Pi Pico W                L9110S                  Motor M35SP7T
┌─────────────────┐         ┌─────────────────┐        ┌─────────────────┐
│ GPIO 2 (Pin 4) ─────────▶│ A-1A            │──────▶ Bobina A1
│ GPIO 3 (Pin 5) ─────────▶│ A-1B            │──────▶ Bobina A2
│ GPIO 4 (Pin 6) ─────────▶│ B-1A            │──────▶ Bobina B1
│ GPIO 5 (Pin 7) ─────────▶│ B-1B            │──────▶ Bobina B2
│ GND ───────────────────▶│ GND             │──────▶ Motor GND
│ 5V  ───────────────────▶│ VCC (5V)        │──────▶ Motor VCC
└─────────────────┘         └─────────────────┘        └─────────────────┘
