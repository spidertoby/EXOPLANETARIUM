from setuptools import setup

setup(
    name = 'EXOPLANETARIUM',
    version = '1.0.0',
    license = 'MIT',
    description = ' Interfaz grafica para visualizar datos de exoplanetas',
    author = 'Fabian Destefano Ulloa - Harry Gonzalez Garrido - Vanessa Meza Aravena - Valentin Muñoz Saldaño',
    install_requires = ['numpy','matplotlib','scipy', 'tkinter', 'pandas']
)