## Nombre del proyecto:
## Descripción del proyecto:
## Nombre de integrantes:
## ID de GitHub: 
## Especificación del API

- ### Volumen de un cubo:
    #### URL
    /cube/volumen/s

    #### Parametros
    - s: Lado del cubo

    #### Salida
    Volumen del cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cubo/volumen/5
  
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cuboReadmeVolumen.png)

- ### Área superficial de un cubo:
    #### URL
    /cube/surfacearea/s

    #### Parametros
    - s: Lado del cubo

    #### Salida
    Área de superficie de un cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cube/surfacearea/5/9
    ![This is an image]()

- ### Volumen de un sólido rectangular:
    #### URL
    /rectangular_solid/volume/l/w/h

    #### Parametros
    - l: Largo del solido rectangular
    - w: Ancho del solido rectangular
    - h: Altura del solido rectangular

    #### Salida
    Volumen de un solido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/rectangular_solid/volume/l/w/h
    ![This is an image]()

- ### Área superficial de un solido rectangular:
    #### URL
    /rectangular_solid/surfacearea/l/w/h

    #### Parametros
    - l: Largo del solido rectangular
    - w: Ancho del solido rectangular
    - h: Altura del solido rectangular

    #### Salida
    Área superficial de un solido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/rectangular_solid/surfacearea/8/5/4
    ![This is an image]()

- ### Volumen de una esfera:
    #### URL
    /sphere/volume/r

    #### Parametros
    - r: Radio de la esfera
    
    #### Salida
    Volumen de una esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/sphere/volume/l/w/h
    ![This is an image]()

- ### Área superficial de una esfera:
    #### URL
    /sphere/surfacearea/l/w/h

    #### Parametros
    - r: Radio de la esfera

    #### Salida
    Área superficial de una esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/sphere/surfacearea/6
    ![This is an image]()

 - ### Volumen de un cilindro circular recto:
    #### URL
    /right_circular_cylinder/volume/r/h

    #### Parametros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto
    
    #### Salida
    Volumen de un cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/right_circular_cylinder/volume/8/9
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/cono%20circular%20recto%20volumen.PNG)

- ### Área superficial de un cilindro circular recto:
    #### URL
    /right_circular_cylinder/surfacearea/r/h

    #### Parametros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto

    #### Salida
    Área superficial de un cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/right_circular_cylinder/surfacearea/8/13
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/cono%20circular%20recto%20areqa.PNG)


 - ### Volumen del toroide:
    #### URL
    /torus/volume/r/R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del toroide
    
    #### Salida
    Volumen de un torus

    #### Ejemplo

    - URL: http://127.0.0.1:8080/torus/volume/1/116
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/toroide%20volumen.PNG)

- ### Área superficial del toroide:
    #### URL
    /torus/surfacearea/r/R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del torus

    #### Salida
    Área superficial del toroide 

    #### Ejemplo

    - URL: http://127.0.0.1:8080/torus/surfacearea/1/12
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/toroide%20area.PNG)


 - ### Volumen del cono o pirámide general:
    #### URL
    /general_cone_or_pyramid/volume/a/h

    #### Parametros
    - a: Área de la base del cono o pirámide general
    - h: Altura del cono o pirámide general
    
    #### Salida
    Volumen del cono o pirámide general

    #### Ejemplo

    - URL: http://127.0.0.1:8080/general_cone_or_pyramid/volume/3/19
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/cono%20general%20o%20piramide%20volumen.PNG)

 - ### Volumen general de un cono circular recto:
    #### URL
    /right_circular_cone/volume/r/h

    #### Parametros
    - r: Radio del cono circular
    - h: Altura del cono circular
    
    #### Salida
    Volumen de un cono circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/right_circular_cone/volume/8/9
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/cono%20circular%20recto%20volumen.PNG)

- ### Área superficial de un cono circular recto:
    #### URL
    /right_circular_cone/surfacearea/r/h

    #### Parametros
    - r: Radio del cono circular recto
    - h: Altura del cono circular recto

    #### Salida
    Área superficial de un cono circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/right_circular_cone/surfacearea/8/13
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/cono%20circular%20recto%20areqa.PNG)

 - ### Volumen general del tronco de cono:
    #### URL
    /frustum_of_a_cone/volume/r/R/h

    #### Parametros
    - r: Radio superior del cono truncado
    - R: Radio de la base del cono truncado
    - h: Altura del cono truncado
    
    #### Salida
    Volumen de un cono truncado

    #### Ejemplo

    - URL: http://127.0.0.1:8080/frustum_of_a_cone/volume/4/5/4
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tronco%20de%20cono%20volumen.PNG)

- ### Área superficial del tronco de cono:
    #### URL
    /frustum_of_a_cone/surfacearea/r/R/s

    #### Parametros
    - r: Radio superior del cono truncado
    - R: Radio de la base del cono truncado
    - s:  Altura inclinada del cono truncado

    #### Salida
    Área superficial de un cono truncado

    #### Ejemplo

    - URL: http://127.0.0.1:8080/frustum_of_a_cone/surfacearea/5/12/4
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tronco%20de%20cono%20area%20superficial.PNG)

 - ### Volumen general de una pirámide cuadrangular:
    #### URL
    /square_pyramid/volume/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrada
    - h: altura de la pirámide cuadrada 
    
    #### Salida
    Volumen de una pirámide cuadrangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/square_pyramid/volume/5/4
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/piramide%20cuadrangular%20volumen.PNG)

- ### Área superficial de la pirámide cuadrangular:
    #### URL
    /square_pyramid/surfacearea/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrangular
    - h: altura de la pirámide cuadrangular

    #### Salida
    Área superficiale de la pirámide cuadrangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/square_pyramid/surfacearea/2/9
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/piramide%20area%20superficial.PNG)

 - ### Volumen general de un tetrahedro regular:
    #### URL
    /regular_tetrahedron/volume/s

    #### Parametros
    - s:  lado del tetrahedro regular
    
    #### Salida
    Volumen del tetraedro regular

    ##### Ejemplo

    - URL: http://127.0.0.1:8080/regular_tetrahedron/volume/10
    -![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tetaedro%20regular%20volumen.PNG)

- ### Área superficial del tetraedro regular:
    #### URL
    /regular_tetrahedron/surfacearea/s

    #### Parametros
    - s: Lado del tetrahedro regular

    #### Salida
    Área superficial del tetraedro regular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/regular_tetrahedron/surfacearea/10
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tetaedro%20regular%20area.PNG)

