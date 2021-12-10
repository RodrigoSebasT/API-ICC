## Nombre del proyecto:
## Descripción del proyecto:
## Nombre de integrantes:
## ID de GitHub: 
## Especificación del API

- ### Volumen de un cubo:
    #### URL
    http://127.0.0.1:8080/cubo/volumen/:s

    #### Parámetros
    - s: Lado del cubo

    #### Salida
    Volumen del cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cubo/volumen/5
  
    ![](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cuboReadmeVolumen.png)

- ### Área superficial de un cubo:
    #### URL
    http://127.0.0.1:8080/cubo/surfacearea/:s
    
    #### Parámetros
    - s: Lado del cubo

    #### Salida
    Área superficial de un cubo

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cubo/surfacearea/5
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cuboReadmeArea.png)

- ### Volumen de un sólido rectangular:
    #### URL
    http://127.0.0.1:8080/solidoRectangular/volumen/:l/:w/:h

    #### Parámetros
    - l: Largo del sólido rectangular
    - w: Ancho del sólido rectangular
    - h: Altura del sólido rectangular

    #### Salida
    Volumen de un sólido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/solidoRectangular/volumen/8/5/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/RectanguloVolumenReadme.png)

- ### Área superficial de un sólido rectangular:
    #### URL
    http://127.0.0.1:8080/solidoRectangular/surfacearea/:l/:w/:h

    #### Parámetros
    - l: Largo del solido rectangular
    - w: Ancho del solido rectangular
    - h: Altura del solido rectangular

    #### Salida
    Área de superficie de un solido rectangular

    #### Ejemplo

    - URL: http://127.0.0.1:8080/solidoRectangular/surfacearea/8/5/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/RectanguloAreaReadme.png)

- ### Volumen de una esfera:
    #### URL
    http://127.0.0.1:8080/esfera/volumen/:r

    #### Parámetros
    - r: Radio de la esfera
    
    #### Salida
    Volumen de una esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/esfera/volumen/6
   
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/VolumenEsferaReadme.png)

- ### Área de superficie de una esfera:
    #### URL
    http://127.0.0.1:8080/esfera/surfacearea/:r

    #### Parámetros
    - r: Radio de la esfera

    #### Salida
    Área superficial de una esfera

    #### Ejemplo

    - URL: http://127.0.0.1:8080/esfera/surfacearea/6
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/AreaEsferaReadme.png)

 - ### Volumen de un cilindro circular recto:
    #### URL
    http://127.0.0.1:8080/cilindroCircularRecto/volumen/:r/:h

    #### Parámetros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto
    
    #### Salida
    Volumen de un cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cilindroCircularRecto/volumen/8/4
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cilindro%20circular%20volumen.PNG)

- ### Área superficial de un cilindro circular recto:
    #### URL
    http://127.0.0.1:8080/cilindroCircularRecto/surfacearea/:r/:h

    #### Parámetros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto

    #### Salida
    Área superficial de un cilindro circular recto

    #### Ejemplo

    - URL: http://127.0.0.1:8080/cilindroCircularRecto/surfacearea/8/13
    
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cilindro%20circular%20area.PNG)


 - ### Volumen de un torus:
    #### URL
    /figurageometrica/torus/volume/r/R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del torus
    
    #### Salida
    Volumen de un torus

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/torus/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de un cilindro circular derecho:
    #### URL
    /figurageometrica/torus/surfacearea/r/R

    #### Parametros
    - r: Radio del tubo
    - R: Radio del torus

    #### Salida
    Área de superficie de un torus

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/torus/surfacearea/3
    - Salida: 27 (o screenshot de la salida en caso existan gráficos)


 - ### Volumen general de un cono o pirámide:
    #### URL
    /figurageometrica/general_cone_or_pyramid/volume/a/h

    #### Parametros
    - a: Área de la base del cono o pirámide
    - h: Altura del cono o piramide
    
    #### Salida
    Volumen de un cono o piramide

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/general_cone_or_pyramid/volume/l/w/h
    ![This is an image]()

 - ### Volumen general de un cono circular recto:
    #### URL
    /figurageometrica/right_circular_cone/volume/r/h

    #### Parametros
    - r: Radio del cono circular
    - h: Altura del cono circular
    
    #### Salida
    Volumen de un cono circular recto

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/right_circular_cone/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de un cono circular recto:
    #### URL
    /figurageometrica/right_circular_cone/surfacearea/r/h

    #### Parametros
    - r: Radio del cono circular recto
    - h: Altura del cono circular recto

    #### Salida
    Área de superficie de un cono circular recto

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/right_circular_cone/surfacearea/3
    ![This is an image]()

 - ### Volumen general de un cono truncado:
    #### URL
    /figurageometrica/frustum_of_a_cone/volume/r/R/h

    #### Parametros
    - r: Radio superior del cono truncado
    - R: Radio de la base del cono truncado
    - h: Altura del cono truncado
    
    #### Salida
    Volumen de un cono truncado

    #### Ejemplo

    - URL: http://127.0.0.1:8080/troncoDeCono/volumen/4/5/4
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/tronco%20de%20cono%20volumen.PNG)

- ### Área de superficie de un cono truncado:
    #### URL
    /figurageometrica/frustum_of_a_cone/surfacearea/r/R/s

    #### Parametros
    - r: Radio superior del cono truncado
    - R: Radio de la base del cono truncado
    - s:  Altura inclinada del cono truncado

    #### Salida
    Área de superficie de un cono truncado

    #### Ejemplo

    - URL: http://127.0.0.1:8080/troncoDeCono/surfacearea/5/12/4
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tronco%20de%20cono%20area%20superficial.PNG)

 - ### Volumen general de una pirámide cuadrada:
    #### URL
    /figurageometrica/square_pyramid/volume/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrada
    - h: altura de la pirámide cuadrada 
    
    #### Salida
    Volumen de una pirámide cuadrada

    #### Ejemplo

    - URL: http://127.0.0.1:8080/piramideCuadrangular/volumen/5/4
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/piramide%20cuadrangular%20volumen.PNG)

- ### Área de superficie de un square_pyramid:
    #### URL
    /figurageometrica/square_pyramid/surfacearea/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrada
    - h: altura de la pirámide cuadrada

    #### Salida
    Área de superficie de la pirámide cuadrada

    #### Ejemplo

    - URL: http://127.0.0.1:8080/piramideCuadrangular/surfacearea/2/9
    ![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/piramide%20area%20superficial.PNG)

 - ### Volumen general de un tetrahedro regular:
    #### URL
    /figurageometrica/regular_tetrahedron/volume/s

    #### Parametros
    - s:  lado del tetrahedro regular
    
    #### Salida
    Volumen de un regular_tetrahedron

    ##### Ejemplo

    - URL: http://127.0.0.1:8080/tetraedroRegular/volumen/10
    -![This is an image](https://github.com/RodrigoSebasT/API-ICC/blob/main/static/tetaedro%20regular%20volumen.PNG)

- ### Área de superficie de un regular_tetrahedron:
    #### URL
    /figurageometrica/regular_tetrahedron/surfacearea/s

    #### Parametros
    - s: Lado del tetrahedro regular

    #### Salida
    Área de superficie de un regular_tetrahedron

    #### Ejemplo

    - URL:  http://127.0.0.1:8080/tetraedroregular/surfacearea/10
    ![This is an image](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/tetaedro%20regular%20area.PNG)

