# EXOPLANETARIUM: Análisis y Visualización de Datos Exoplanetarios.

## Descripción

**Exoplanetarium** es un programa que adquiere datos de planetas exoplanetarios desde [Exoplanet.eu](https://exoplanet.eu/catalog/), los procesa y los gráfica en una interfaz gráfica de usuario (GUI). l programa genera gráficos de diversas características de los exoplanetas, tales como la velocidad radial, mapa de temperaturas superficiales, hasta diagramas de Hertzsprung-Russell (H-R) y simulaciones de orbita, junto a otras características relevantes.
Su objetivo es ser amigable e intuitiva con el usuario, proporcionando información sobre los gráficos y como interpretarlos.

## Integrantes

- Fabian Destefano Ulloa
- Harry González Garrido
- Vanessa Meza Aravena
- Valentin Muñóz Saldaño

## Características

- Adquisición de datos exoplanetarios desde la base de datos [Exoplanet.eu](https://exoplanet.eu/catalog/)
- Procesamiento y limpieza de datos
- Generación de gráficos interactivos tipo:
  - Histograma y Scatter Plots de distintas caractersticas
  - Mapa de temperaturas superficiales
  - Diagrama de Hertzsprung-Russell (H-R)
  - Simulación de órbitas exoplanetarias




## Instalación

La instalación de este programa requiere ciertos pasos. A continuación, se describen las instrucciones tanto para Linux como para Windows.

### Para Linux:
El link de la carpeta zip es el siguiente: https://drive.google.com/file/d/1xwVjpb-s7I4eBq-gT8sfbgM7IJHptPrk/view?usp=sharing 

1. Descarga y descomprime el archivo `Exoplanetarium_Linux.zip`.

    ```sh
    unzip Exoplanetarium_Linux.zip
    ```

2. Navega a la carpeta `main` dentro de `Exoplanetarium_Linux`:

    ```sh
    cd Exoplanetariuma_Linux/main
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

1. Descarga y descomprime el archivo `Exoplanetarium_Windows.zip`.

    - Haz clic derecho en el archivo y selecciona "Extraer todo..." o utiliza una herramienta como WinRAR o 7-Zip.

2. Navega a la carpeta `main` dentro de `Exoplanetarium_Windows`. Puedes hacerlo utilizando el Explorador de archivos o desde la línea de comandos.

3. Abre una terminal en la carpeta `main`:

    - Haz clic derecho en la carpeta `main` mientras mantienes presionada la tecla Shift y selecciona "Abrir ventana de PowerShell aquí" o "Abrir ventana de comando aquí".

4. Utiliza el siguiente comando para instalar el programa:

    ```sh
    python -m pip install .
    ```

5. Una vez completada la instalación, para correr la interfaz, utiliza el siguiente comando:

    ```sh
    python main.py
    ```

 

## Uso
Previamente asegúrese que tiene instalado su paquete. Cuando se asegure de ello podrá importar las diferentes funcionalidades del programa
como la simulacion de orbitas planetarias, generar graficas de temperatura superficial o diagramas HR.

Aclaración, los datos con los que trabaja Exoplanetarium ya están integrados dentro de la terminal, los cuales son extraídos directamente desde la página y se actualizan automáticamente a medida que la página añade nuevos registros.

## Dependencias
- Python [3.8, 3.10]
- Numpy [1.26]
- Pandas
- pip (astropy [6.0.0], matplotlib [3.8.2], scipy [1.13.0], beautifulsoup4 [4.12.2], requests [2.31.0], selenium [4.10.0], webdriver-manager [3.8.6] )
- setuptools 

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulte el archivo [LICENSE.txt](LICENSE.txt) para obtener más detalles.

