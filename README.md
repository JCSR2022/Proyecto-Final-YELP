# PF-YELP

## Metricas

Son indicadores que mide la empresa, usando todos los datos que tiene a disposicion, ej. numero de ordenes por dia en un restaurante

### KPI’s (Key Performance Indicator)

Es una metrica **clave,** estas son solo unas cuantas respecto a las metricas pero tienen un alto impacto en el negocio, por lo que mejorarlas representara un inpacto positivo para la empresa,

entendemos asi que todos los KPI’s son metricas pero no todas las metricas son KPI’s

1)porcentaje de crecimiento del promedio de estrellas(calificación):
    PCC= (promedio estrellas año 2) - (promedio estrellas año 1) / ((promedio estrellas año 1)

2) crecimiento de reviews:
    PCR = (cantidad de reviews año 2) - (cantidad de reviews año 1) /((cantidad de reviews año 1))

3) popularidad: 
    PO = promedio(polaridad*(1-subjetividad))

4) cantidad de sucursales por rubro cerradas por rubro
    CSC = cantidad de sucursales cerradas) / cantidad de sucursales totales por rubro *100


### Objetivos:

- Predecir cuales son los rubros de negocios que mas creceran o decaeran
- Predecir la localizacin mas conveniente de nuevos locales de estos negocios evaluados
- Implementar un sistema de recomendaciones para usuarios

### Alcance del proyecto

### stack tecnológico

### Diccionario de datos

users:
'n_user_id': integer user code,
'user_id': alphanumeric user code, 
'review_count': number of reviews made by the user, 
'yelping_since': user registration date, 
'useful': number of useful ,
'funny', 
'cool', 
'friends', 
'fans', 
'average_stars'