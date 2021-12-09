## Nombre del proyecto:
## Descripción del proyecto:
## Nombre de integrantes:
## ID de GitHub: 
## Especificación del API

- ### Volumen de un cubo:
    #### URL
    figurageometrica/cube/volumen/s

    #### Parametros
    - s: Lado del cubo

    #### Salida
    Volumen del cubo

    #### Ejemplo

    - URL: localhost:9000/cube/volumen/3
   
    ![Imagen de un cubo](https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/cuboReadmeVolumen.png)

- ### Área de superficie de un cubo:
    #### URL
    figurageometrica/cube/surfacearea/s

    #### Parametros
    - s: Lado del cubo

    #### Salida
    Área de superficie de un cubo

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/cube/surfacearea/3
    ![This is an image]()

- ### Volumen de un sólido rectangular:
    #### URL
    /figurageometrica/rectangular_solid/volume/l/w/h

    #### Parametros
    - l: Largo del solido rectangular
    - w: Ancho del solido rectangular
    - h: Altura del solido rectangular

    #### Salida
    Volumen de un solido rectangular

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/rectangular_solid/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de un solido rectangular:
    #### URL
    figurageometrica/rectangular_solid/surfacearea/l/w/h

    #### Parametros
    - l: Largo del solido rectangular
    - w: Ancho del solido rectangular
    - h: Altura del solido rectangular

    #### Salida
    Área de superficie de un solido rectangular

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/rectangular_solid/surfacearea/3
    ![This is an image]()

- ### Volumen de una esfera:
    #### URL
    /figurageometrica/sphere/volume/r

    #### Parametros
    - r: Radio de la esfera
    
    #### Salida
    Volumen de una esfera

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/sphere/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de una esfera:
    #### URL
    figurageometrica/sphere/surfacearea/l/w/h

    #### Parametros
    - r: Radio de la esfera

    #### Salida
    Área de superficie de una esfera

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/sphere/surfacearea/3
    ![This is an image]()

 - ### Volumen de un cilindro circular recto:
    #### URL
    /figurageometrica/right_circular_cylinder/volume/r/h

    #### Parametros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto
    
    #### Salida
    Volumen de un cilindro circular recto

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/right_circular_cylinder/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de un cilindro circular recto:
    #### URL
    /figurageometrica/right_circular_cylinder/surfacearea/r/h

    #### Parametros
    - r: Radio del cilindro circular recto
    - h: Altura del clindro circular recto

    #### Salida
    Área de superficie de un cilindro circular recto

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/right_circular_cylinder/surfacearea/3
    ![This is an image]()


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

    - URL: localhost:9000/figurageometrica/frustum_of_a_cone/volume/l/w/h
    ![This is an image]()

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

    - URL: localhost:9000/figurageométrica/frustum_of_a_cone/surfacearea/3
    ![This is an image]()

 - ### Volumen general de una pirámide cuadrada:
    #### URL
    /figurageometrica/square_pyramid/volume/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrada
    - h: altura de la pirámide cuadrada 
    
    #### Salida
    Volumen de una pirámide cuadrada

    #### Ejemplo

    - URL: localhost:9000/figurageometrica/square_pyramid/volume/l/w/h
    ![This is an image]()

- ### Área de superficie de un square_pyramid:
    #### URL
    /figurageometrica/square_pyramid/surfacearea/s/h

    #### Parametros
    - s: Lado de la pirámide cuadrada
    - h: altura de la pirámide cuadrada

    #### Salida
    Área de superficie de la pirámide cuadrada

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/square_pyramid/surfacearea/3
    ![This is an image]()

 - ### Volumen general de un tetrahedro regular:
    #### URL
    /figurageometrica/regular_tetrahedron/volume/s

    #### Parametros
    - s:  lado del tetrahedro regular
    
    #### Salida
    Volumen de un regular_tetrahedron

    ##### Ejemplo

    - URL: localhost:9000/figurageometrica/regular_tetrahedron/volume/l/w/h
    -![This is an image]()

- ### Área de superficie de un square_pyramid:
    #### URL
    /figurageometrica/regular_tetrahedron/surfacearea/s

    #### Parametros
    - s: Lado del tetrahedro regular

    #### Salida
    Área de superficie de un regular_tetrahedron

    #### Ejemplo

    - URL: localhost:9000/figurageométrica/regular_tetrahedron/surfacearea/3
    ![This is an image]()

