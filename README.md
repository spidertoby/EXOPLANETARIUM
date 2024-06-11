# EXOPLANETARIUM: Análisis y Visualización de Datos Exoplanetarios

## Descripción

**Exoplanetarium** es un programa que adquiere datos de planetas exoplanetarios desde [Exoplanet.eu](https://exoplanet.eu/catalog/), los procesa y los grafica en una interfaz gráfica de usuario (GUI). El programa simula las órbitas de los exoplanetas y genera gráficos de diferentes datos, como la velocidad radial, mapa de temperaturas superficiales, diagramas de Hertzsprung-Russell (H-R), diagramas de órbita y otras características relevantes de los exoplanetas.

## Integrantes

- Fabian Destefano Ulloa
- Harry González Garrido
- Vanessa Meza Aravena
- Valentin Muñóz Saldaño

## Características

- Adquisición de datos exoplanetarios desde la base de datos [Exoplanet.eu](https://exoplanet.eu/catalog/)
- Procesamiento y limpieza de datos
- Simulación de órbitas exoplanetarias
- Generación de gráficos interactivos de:
  - Velocidad radial
  - Mapa de temperaturas superficiales
  - Diagramas de Hertzsprung-Russell (H-R)
  - Diagramas de órbita
  - Otras características relevantes de los exoplanetas




## Instalación

La instalación de este programa requiere ciertos pasos. A continuación, se describen las instrucciones tanto para Linux como para Windows.

### Para Linux:

1. Descarga y descomprime el archivo `EXOPLANETARIUM.zip`.

    ```sh
    unzip EXOPLANETARIUM.zip
    ```

2. Navega a la carpeta `test` dentro de `src`:

    ```sh
    cd EXOPLANETARIUM/src/test
    ```

3. Utiliza el siguiente comando para instalar el programa:

    ```sh
    python -m pip install .
    ```

4. Una vez completada la instalación, para correr la interfaz, utiliza el siguiente comando:

    ```sh
    python main.py
    ```

### Para Windows:

1. Descarga y descomprime el archivo `EXOPLANETARIUM.zip`.

    - Haz clic derecho en el archivo y selecciona "Extraer todo..." o utiliza una herramienta como WinRAR o 7-Zip.

2. Navega a la carpeta `test` dentro de `src`. Puedes hacerlo utilizando el Explorador de archivos o desde la línea de comandos.

3. Abre una terminal en la carpeta `test`:

    - Haz clic derecho en la carpeta `test` mientras mantienes presionada la tecla Shift y selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comando aquí".

4. Utiliza el siguiente comando para instalar el programa:

    ```sh
    python -m pip install .
    ```

5. Una vez completada la instalación, para correr la interfaz, utiliza el siguiente comando:

    ```sh
    python main.py
    ```

 

## Uso
Primeramente asegura que tienes instalado tu paquete. Cuando te asegures de ello podrás importar las diferentes funcionalidades del programa
como la simulacion de orbitas planetarias, generar graficas de temperatura superficial, velocidad o diagramas HR.

Aclaracion, los datos entregados a Exoplanetarium deben estar proporcionados por el usuario, aparecerá una pestaña para que se pueda seleccionar el archivo y subirlo.
## Dependencias
- Python [3.8, 3.10]
- Numpy [1.26]
- Pandas
- pip (astropy [6.0.0], matplotlib [3.8.2], scipy [1.13.0])
- setuptools 

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE) para obtener más detalles.
