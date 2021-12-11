# Geometría Para Todos

## Descripción del proyecto:

Creamos una API que ayuda a calcular el volumen y el área superficial de un figura geometrica del espacio.
En esta primera version, decidimos implementar la API para diez figuras geometricas. 
1. El cubo
2. El sólido rectangular
3. La esfera
4. El cilindro circular recto
5. El toroide
6. El cono o pirámide general (para esta figura solo se implemento su volumen)
7. El cono circular recto
8. El tronco de un cono
9. La pirámide cuadrangular
10. El tetraedro regular

## Instalación:

Necesitas las siguientes herramientas para ejecutar nuestra API

- Python 3.0+
- Flask 2.0+

Una vez instalado python 3.0+, ejecuta el siguiente comando

`pip3 install flask`

## Ejecución de la API:

Una vez instalados todos los programas necesarios, solo necesitas clonar nuestro repositorio:

`git clone https://github.com/RodrigoSebasT/API-ICC.git`

Despues de ello, entra a nuestro proyecto y ejecútalo:

`python3 server.py`

## Nombre de integrantes:
1. Rodrigo Sebastian Trujillo Mirano
2. John Rodrigo Monroy Angeles
3. Yovana Ramos Mamani


## Especificación del API

- ### Volumen de un cubo:
    #### URL
    http://127.0.0.1:8080/cubo/volumen/:s

    #### Parámetros
    - s: Lado del cubo

    #### Salida
    - Volumen del cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cubo/volumen/5
  
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cuboReadmeVolumen.png)

- ### Área superficial de un cubo:
    #### URL
    http://127.0.0.1:8080/cubo/surfacearea/:s
    
    #### Parámetros
    - s: Lado del cubo

    #### Salida
    - Área superficial del cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cubo/surfacearea/5
    
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cuboReadmeArea.png)

- ### Volumen de un sólido rectangular:
    #### URL
    http://127.0.0.1:8080/solidoRectangular/volumen/:l/:w/:h

    #### Parámetros
    - l: Largo del sólido rectangular
    - w: Ancho del sólido rectangular
    - h: Altura del sólido rectangular

    #### Salida
    - Volumen del sólido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/solidoRectangular/volumen/8/5/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/RectanguloVolumenReadme.png)

- ### Área superficial de un sólido rectangular:
    #### URL
    http://127.0.0.1:8080/solidoRectangular/surfacearea/:l/:w/:h

    #### Parámetros
    - l: Largo del sólido rectangular
    - w: Ancho del sólido rectangular
    - h: Altura del sólido rectangular

    #### Salida
    - Área superficial del sólido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/solidoRectangular/surfacearea/8/5/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/RectanguloAreaReadme.png)

- ### Volumen de una esfera:
    #### URL
    http://127.0.0.1:8080/esfera/volumen/:r

    #### Parámetros
    - r: Radio de la esfera
    
    #### Salida
    - Volumen de la esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/esfera/volumen/6
   
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/VolumenEsferaReadme.png)

- ### Área de superficie de una esfera:
    #### URL
    http://127.0.0.1:8080/esfera/surfacearea/:r

    #### Parámetros
    - r: Radio de la esfera

    #### Salida
    - Área superficial de la esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/esfera/surfacearea/6
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/AreaEsferaReadme.png)

 - ### Volumen de un cilindro circular recto:
    #### URL
    http://127.0.0.1:8080/cilindroCircularRecto/volumen/:r/:h

    #### Parámetros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto
    
    #### Salida
    - Volumen del cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cilindroCircularRecto/volumen/8/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cilindro%20circular%20volumen.PNG)

- ### Área superficial de un cilindro circular recto:
    #### URL
    http://127.0.0.1:8080/cilindroCircularRecto/surfacearea/:r/:h

    #### Parámetros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto

    #### Salida
    - Área superficial del cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cilindroCircularRecto/surfacearea/8/13
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cilindro%20circular%20area.PNG)

 - ### Volumen de un toroide:
    #### URL
    http://127.0.0.1:8080/toroide/volumen/:r/:R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del toroide
    
    #### Salida
    - Volumen del toroide

    #### Ejemplo

    - URL: http://127.0.0.1:8080/toroide/volumen/1/116

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/toroide%20volumen.PNG)

- ### Área superficial de un toroide:
    #### URL
    http://127.0.0.1:8080/toroide/surfacearea/:r/:R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del toroide

    #### Salida
    - Área superficial del toroide

    #### Ejemplo

    - URL: http://127.0.0.1:8080/toroide/surfacearea/1/12

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/toroide%20area.PNG)

 - ### Volumen de un cono o pirámide general:
    #### URL
    http://127.0.0.1:8080/conoGeneraloPiramide/volumen/:a/:h

    #### Parametros
    - a: Área de la base del cono o pirámide general
    - h: Altura del cono o piramide general
    
    #### Salida
    - Volumen del cono o pirámide general

    #### Ejemplo

    - URL: http://127.0.0.1:8080/conoGeneraloPiramide/volumen/10/7

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/conoGeneralVolumen.png)

 - ### Volumen de un cono circular recto:
    #### URL
    http://127.0.0.1:8080/conoCircularRecto/volumen/:r/:h

    #### Parametros
    - r: Radio del cono circular recto
    - h: Altura del cono circular recto
    
    #### Salida
    - Volumen del cono circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/conoCircularRecto/volumen/5/9
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/VolumenConoRegularReadme.png)

- ### Área superficial de un cono circular recto:
    #### URL
    http://127.0.0.1:8080/conoCircularRecto/surfacearea/:r/:h

    #### Parámetros
    - r: Radio del cono circular recto
    - h: Altura del cono circular recto

    #### Salida
    - Área superficial del cono circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/conoCircularRecto/surfacearea/5/9
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/AreaConoRegularReadme.png)

 - ### Volumen de un tronco de cono:
    #### URL
    http://127.0.0.1:8080/troncoDeCono/volumen/:r/:R/:h

    #### Parametros
    - r: Radio de la base superior del tronco de cono
    - R: Radio de la base inferior del tronco de cono
    - h: Altura del tronco de cono
    
    #### Salida
    - Volumen de un cono truncado

    #### Ejemplo

    - URL: http://127.0.0.1:8080/troncoDeCono/volumen/4/5/4
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/tronco%20de%20cono%20volumen.PNG)

- ### Área superficial del cono de tronco:
    #### URL
    /figurageometrica/frustum_of_a_cone/surfacearea/:r/:R/:s

    #### Parametros
    - r: Radio de la base superior del tronco de cono
    - R: Radio de la base inferior del tronco de cono
    - s: Longitud del lado lateral del tronco de cono

    #### Salida
    - Área superficial del cono de tronco

    #### Ejemplo

    - URL: http://127.0.0.1:8080/troncoDeCono/surfacearea/5/12/4
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tronco%20de%20cono%20area%20superficial.PNG)

 - ### Volumen de una pirámide cuadrangular:
    #### URL
    http://127.0.0.1:8080/piramideCuadrangular/volumen/:s/:h

    #### Parametros
    - s: Lado de la pirámide cuadradrangular
    - h: Altura de la pirámide cuadrangular 
    
    #### Salida
    - Volumen de la pirámide cuadrangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/piramideCuadrangular/volumen/5/4

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/piramide%20cuadrangular%20volumen.PNG)

 - ### Área superficial de una pirámide cuadrangular:
    #### URL
    http://127.0.0.1:8080/piramideCuadrangular/surfacearea/:s/:h

    #### Parámetros
    - s: Lado de la pirámide cuadrangular
    - h: Altura de la pirámide cuadrangular

    #### Salida
    - Área superficial de la pirámide cuadrangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/piramideCuadrangular/surfacearea/2/9

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/piramide%20area%20superficial.PNG)

 - ### Volumen del tetraedro regular:
    #### URL
    http://127.0.0.1:8080/tetraedroRegular/volumen/:s

    #### Parámetros
    - s: Lado del tetraedro regular
    
    #### Salida
    - Volumen del tetraedro regular

    ##### Ejemplo

    - URL: http://127.0.0.1:8080/tetraedroRegular/volumen/10
  
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/tetaedro%20regular%20volumen.PNG)

- ### Área superficial del tetraedro regular:
    #### URL
    http://127.0.0.1:8080/tetraedroregular/surfacearea/:s

    #### Parametros
    - s: Lado del tetraedro regular

    #### Salida
    - Área superficial del tetraedro regular

    #### Ejemplo

    - URL:  http://127.0.0.1:8080/tetraedroregular/surfacearea/10

    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/tetaedro%20regular%20area.PNG)

