# Aula de Fluidos

**Aula de Fluidos** es una plataforma web educativa para el curso de Mecánica de Fluidos. Permite a los estudiantes consultar teoría, resolver ejercicios interactivos y realizar cálculos prácticos de forma dinámica.

## 🚀 Características principales

1. **Generalidades / Propiedades de los Fluidos**
    - Teoría de densidad, viscosidad, gravedad específica, etc.
    - Calculadora de densidad, peso específico y coeficiente de compresibilidad.
    - Conversión de unidades (métrico ↔ inglés).
    - Ejercicio de comparación de flujos Newtonianos vs. no Newtonianos.

2. **Presión e Introducción a la Estática de Fluidos**
    - Teoría de presión hidrostática.
    - Cálculo de presión via manómetro (ρ·g·h).
    - Fuerza sobre superficies sumergidas (F = p·A).
    - Visualización de flotación y metacentro.

3. **Cinemática de Fluidos**
    - Descripción de enfoques Lagrangiano y Euleriano.
    - Aplicación de la ecuación de Bernoulli con formulario interactivo.
    - Simulador de medidor Venturi y Teorema de Torricelli.

4. **Flujo en Tuberías**
    - Determinación del número de Reynolds.
    - Cálculo de pérdidas por fricción (ecuación de Darcy).
    - Diagrama de Moody interactivo.
    - Pérdidas menores en accesorios (válvulas, codos).

5. **Potencia y Eficiencia de Máquinas de Flujo**
    - Cálculo de potencia de bombas según caudal y altura.
    - Estimación de eficiencia de sistemas de bombeo.

6. **Sistemas de Tuberías en Serie y Paralelo**
    - Resolución de caudales y pérdidas en configuraciones múltiples.
    - Formulario para múltiples tramos de tubería.

7. **Análisis Dimensional**
    - Introducción a la teoría de similitud.
    - Calculadora de coeficientes adimensionales.

8. **Visualizaciones**
    - Gráficos con Matplotlib (perfiles de velocidad, distribución de presión).
    - Opcional: gráficos interactivos con Plotly.js.

## 🛠 Tecnologías

- **Back-end:** Python, Flask
- **Plantillas:** Jinja2, HTML5, CSS3
- **Gráficos:** Matplotlib (y/o Plotly)
- **Gestión de variables de entorno:** python-dotenv
- **Entorno de desarrollo:** virtualenv / venv

## 📥 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Manuuell/AulaFluidos.git
   cd AulaFluidos

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate     # Linux / macOS
   .venv\Scripts\activate        # Windows

3. Instala dependencias
   ```bash
   pip install -r requirements.txt
