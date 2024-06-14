import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#leer datos
data = pd.read_csv("exoplanet_data.csv")
print(data.columns)

#dataframe con los datos para orbitas
orbital_data = pd.DataFrame(data, columns=["star_name", "star_mass", "name", "mass", "orbital_period", "semi_major_axis", "eccentricity","omega", "tperi"])
orbital_data_clean = orbital_data.dropna()#eliminar valores nulos NaN

#dataframe con los nombres de las estrellas anfitrionas
star_names = pd.DataFrame(orbital_data_clean, columns=["star_name"])
print(star_names)

#funcion que extrae los datos orbitales de los palnetas de una estrella especifica
def datos_orbita_sistema(star_name):
    """
    - recibe el nombre de una estrella y creo un dataframe con los datos de los planetas que la orbitan
    - los datos son tomados dataframe orbital_data anteriormente definido fuera de la funcion
    - los datos incluidos estan pensados para ser de utilidad al graficar orbitas
    """
    star_planets = orbital_data_clean[orbital_data_clean['star_name']==star_name]
    return star_planets

#podriamos poner la cantidad de planetas que tiene la estrella junto al nombre
#en la lista de la interfaz grafica
def N_planetas_x_estrella(star_name):
    """
    - funcion que calcula el numero de planetas que orbitan una estrella
    """
    data = datos_orbita_sistema(star_name)
    return len(data)

#funcion para calcular orbitas
def calcular_orbita(semi_major_axis, eccentricity, omega, tperi, T, num=100):
    """
    Funcion de calculo de orbitas
    nota: diseñada para trabajar con el dataframe orbital_data_clean definido anteriormente
    y usarse dentro de la animacion de los graficos, vease como parte complementaria y no para usarse
    de manera independiemte.
    - semi_major_axis: eje semimayor
    - eccentricity: exenctricidad
    - omega: velocidad angular
    - tperi: tiempo periastro
    - T: periodo orbital
    - num: cantidad de instantes de tiempo para calcular la orbita, por defecto 100
    """
    omega_rad = np.radians(omega)
    t = np.linspace(0, T, num)
    M = 2 * np.pi * (t - tperi) / T
    E = M
    for _ in range(100):
        E = M + eccentricity * np.sin(E)
    x = semi_major_axis * (np.cos(E) - eccentricity)
    y = semi_major_axis * np.sqrt(1 - eccentricity**2) * np.sin(E)
    x_rot = x * np.cos(omega_rad) - y * np.sin(omega_rad)
    y_rot = x * np.sin(omega_rad) + y * np.cos(omega_rad)
    return x_rot, y_rot



#util para determinar la posicion de la estrella en su sistema
#el baricentro corresponde al centro de masa de un sistema y el punto
#al que orbitan en torno la estrella y sus planetas
#suele estar cerca del centro de la estrella pero puede verse afectado por planetas masivos
def calcular_baricentro(star_name):
    """
     Calcula el baricentro de un sistema planetario
    - recibe el nombre de una estrella presente en el dataframe orbital_data_clean
    """
    star_planets = datos_orbita_sistema(star_name)
    star_mass = star_planets.iloc[0]['star_mass']
    total_mass = star_mass + star_planets['mass'].sum()
    x_pos, y_pos = 0, 0
    for _, planet in star_planets.iterrows():
        semi_major_axis = planet['semi_major_axis']
        eccentricity = planet['eccentricity']
        omega = planet['omega']
        tperi = planet['tperi']
        planet_mass = planet['mass']
        distance_to_periapsis = semi_major_axis * (1 - eccentricity)
        x_orbit = distance_to_periapsis * np.cos(np.radians(omega))
        y_orbit = distance_to_periapsis * np.sin(np.radians(omega))
        x_pos += x_orbit * planet_mass
        y_pos += y_orbit * planet_mass
    x_pos /= total_mass
    y_pos /= total_mass
    return x_pos, y_pos

#determinar posicion de la estrella en su sistema
def calcular_posicion_estrella(star_name):
    """
     Calcula la posicion de una estrella dentro de su sistema planetario
    utilizando el baricentro, calculado por la funcion calcular_baricentro, 
    y las masas de los planetas y su estrella.
    - recibe el nombre de una estrella presente en el dataframe orbital_data_clean
      """
    baricentro_x, baricentro_y = calcular_baricentro(star_name)
    star_planets = datos_orbita_sistema(star_name)
    star_mass = star_planets.iloc[0]['star_mass']
    total_mass = star_mass + star_planets['mass'].sum()
    star_x = -baricentro_x * (star_mass / total_mass)
    star_y = -baricentro_y * (star_mass / total_mass)
    return star_x, star_y

#se asegura de que todas las orbitas aparezcan completas en los graficos
def obtener_limites_orbita(star_name):
    """
     Funcion definida para modificar los limites de los graficos segun el
    sistema planetario ingresado lo requiera y pder visualizar de mejor manera las orbitas
    de todos los cuerpos del sistema
    - recibe el nombre de una estrella presente en el dataframe orbital_data_clean
    """
    star_planets = datos_orbita_sistema(star_name)
    min_x, max_x = np.inf, -np.inf
    min_y, max_y = np.inf, -np.inf
    for _, planet in star_planets.iterrows():
        x, y = calcular_orbita(
            semi_major_axis=planet['semi_major_axis'],
            eccentricity=planet['eccentricity'],
            omega=planet['omega'],
            tperi=planet['tperi'],
            T=planet['orbital_period'],
            num=1000
        )
        min_x = min(min_x, np.min(x))
        max_x = max(max_x, np.max(x))
        min_y = min(min_y, np.min(y))
        max_y = max(max_y, np.max(y))
    return min_x, max_x, min_y, max_y

#generar los graficos
def animar_orbitas(star_name):
    """
    Crea gráficos 2D animados de las órbitas de los planetas en un
    sistema planetario.
    - Recibe el nombre de una estrella presente en el dataframe orbital_data_clean
    """
    star_planets = datos_orbita_sistema(star_name)
    fig, ax = plt.subplots(figsize=(10, 10))
    
    star_x, star_y = calcular_posicion_estrella(star_name)
    
    ax.plot(star_x, star_y, 'yo', label='Estrella Anfitriona', markersize=12)
    
    min_x, max_x, min_y, max_y = obtener_limites_orbita(star_name)
    
    planet_lines = []
    planet_markers = []
    for _, planet in star_planets.iterrows():
        x, y = calcular_orbita(
            semi_major_axis=planet['semi_major_axis'],
            eccentricity=planet['eccentricity'],
            omega=planet['omega'],
            tperi=planet['tperi'],
            T=planet['orbital_period'],
            num=1000
        )
        line, = ax.plot(x, y, label=planet['name'])
        planet_lines.append(line)
        marker, = ax.plot([], [], 'o', color=line.get_color())
        planet_markers.append(marker)
    
    def init():
        margin = 0.2
        ax.set_xlim(min_x - margin, max_x + margin)
        ax.set_ylim(min_y - margin, max_y + margin)
        ax.set_xlabel('Distancia (AU)')
        ax.set_ylabel('Distancia (AU)')
        ax.set_title(f'Órbitas de los exoplanetas alrededor de [{star_name}]')
        ax.legend()
        ax.grid(True)
        return planet_markers
    
    def update(frame):
        for marker, (_, planet) in zip(planet_markers, star_planets.iterrows()):
            x, y = calcular_orbita(
                semi_major_axis=planet['semi_major_axis'],
                eccentricity=planet['eccentricity'],
                omega=planet['omega'],
                tperi=planet['tperi'],
                T=planet['orbital_period'],
                num=1000
            )
            marker.set_data(x[frame], y[frame])
        return planet_markers

    ani = FuncAnimation(fig, update, frames=1000, init_func=init, blit=True, interval=50, repeat=True)
    plt.show()

#ejemplo de grafico
animar_orbitas("XO-3")