<<<<<<< HEAD
from flask import Flask, render_template, flash, url_for
from math import pi
=======
from flask import Flask, render_template
import math
>>>>>>> e83ca76c16bc3b8f225e2e52e13d5159ce498e52

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

<<<<<<< HEAD
#no editar nada de arriba
@app.route('/toroide/<opcion>/<r>/<R>', methods=['GET'])
def calcularToroide(opcion,r,R):
    r = float(r)
    R = float(R)
    if opcion.lower()=='volumen':
        return """<!DOCTYPE html><head><style type="text/css"> *{
                    background-color: black;
                    color:white
                }

                .toro {
                    position: relative;
                }

                .toro .img_toro img{
                    border-radius: 30px;
                    width: 140%;
                    height: 100%;

                }

                .toro .img_toro {
                    position: absolute;
                    left: 450px;
                    top: 60px;
                }

                </style>
                    <title>Document</title></head>
                <body>
                <div class="toro">"""+"""<p>r: radio del tubo<br>R: radio del toroide<br>r = {}<br>R = {}<br>Volumen: {}</p>""".format(r,R,(2*R*((pi)**2)*((r)**2)))+"""
                        <div class='img_toro'><img src={}>
                        </div>
                    </div>
                </body></html>""".format("https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/toro.png")


    elif opcion.lower()=='surfacearea':
        return f"r: radio del tubo\nR: radio del toroide\nr={r}\nR={R}\nSurface Area: {4*R*((pi)**2)*r}"




@app.route('/tetraedroregular/<opcion>/<l>', methods=['GET'])
def calcularTetraedro(opcion,l):
    l = float(l)
    if opcion.lower()=='volumen':
        return f"l: lado del tetredro regular\nl={l}\nVolumen: {((2**(1/2))*(l**3))/12}"

    elif opcion.lower()=='surfacearea':
        return """<head><style type="text/css">
                    body{background-color:black;color: white;}
            .container {
                width: 150px;
                height: 150px;
                margin: 50px auto;
                position: relative;
            }

            .container .r1 {
                color: white;
                font-size: 30px;
                position: absolute;
                top: 50px;
                right: -30px;
            }

            .container .r2 {
                color: white;
                font-size: 30px;
                position: absolute;
                top: 150px;
                right: -20px;
            }

            .container .r3 {
                color: white;
                font-size: 30px;
                position: absolute;
                top: 175px;
                right: 100px;
            }

            #cube {
                width: 100%;
                height: 100%;
                position: absolute;
                top:30px;
            }

            #cube figure {
                width: 100%;
                height: 100%;
                margin: 0;
                border: 2px solid;
                position: absolute;
                background: hsla(0, 0%, 100%, 0.5);
            }

            #cube .back {
                /*background: hsla(0, 100%, 50%, 0.5);*/
                /*background: white;*/
                border-color: white;
            }



            .container {
                perspective: 350px;
            }

            #cube {
                transform-style: preserve-3d;
            }

            #cube .back {
                transform: rotateX(0deg);
            }

            #cube .left {
                transform: rotateY(60deg);
                border-color: white;

            }

            #cube .bottom {
                transform: rotateX(60deg);
                border-color: white;
            }

            #cube .back {
                transform: rotateX(0deg) rotateY(-20deg) translateZ(-75px) translateX(0px); /*referencia*/
            }
            
            #cube .left {
            transform: rotateY(70deg) translateZ(-75px);

            }

            #cube .bottom {
            transform: rotateX(90deg) translateZ(-75px) rotateZ(20.1deg);
            }

            #cube .front {
                transform: rotateX(0deg) translateZ(75px) rotateY(-20deg) translateX(-28px);
                border-color: white;
            }

            #cube .right {
                transform: rotateY(70deg) translateZ(75.5px);
                border-color: white;
            }

            #cube .top {
                transform: rotateX(90deg) translateZ(75px) rotateZ(20.1deg) translateZ(1.1px);
                border-color: white;
            }
                    </style>
                    </head>
                    <body>
                    """+"""<p>l: lado del tetredro regular<br>l={}<br>Surface Area: {}</p>""".format(l,(3**(1/2))*(l**2))+"""<div class="container">
                                    <div id="cube">
                                        <figure class="back"></figure>
                                        <figure class="left"></figure>
                                        <figure class="bottom"></figure>
                                        <figure class="right"></figure>
                                        <figure class="top"></figure>
                                        <figure class="front"></figure>  <!--probar-->
                                    </div>
                                    <p class="r1">r</p>
                                    <p class="r2">r</p>
                                    <p class="r3">r</p>
                                </div>
                                
                                
                            </body>"""
=======
@app.route('/name/<name>', methods=['GET'])
def ejemplo(name):
    return f"Hola, {name}"
#volume cube
@app.route('/figurageometrica/cube/volume/<s>', methods=['GET'])
def cube_volume(s):

    entero = int(s)
    volumen = entero**3
    return (f"El volumen del cubo es: {str(volumen)}")

#surfacearea cube
@app.route('/figurageometrica/cube/surfacearea/<s>', methods=['GET'])
def cube_surfacearea(s):

    entero = int(s)
    surfacearea = 6*(entero**2)
    return(f"La surfacearea del cubo es:  {str(surfacearea)}")

#volume rectangular_solid
@app.route('/figurageometrica/rectangular_solid/volume/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_volume(l,w,h):

    volume = int(l)*int(w)*int(h)
    return(f"El volumen de rectangular_solid es:  {str(volume)}")

#surfacearea rectangular_solid
@app.route('/figurageometrica/rectangular_solid/surfacearea/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_surfacearea(l,w,h):

    surfacearea = 2*(int(l)*int(w) + int(h)*int(l) + int(w)*int(h))
    return(f"La surfacearea de rectangular_solid es:  {str(surfacearea)}")

#volume sphere
@app.route('/figurageometrica/sphere/volume/<r>', methods=['GET'])
def sphere_volume(r):
    
    volume = (int(r)**3)*(4/3)*math.pi
    return(f"El volume de la sphere es:  {str(volume)}")

#surfacearea sphere
@app.route('/figurageometrica/sphere/surfacearea/<r>', methods=['GET'])
def sphere_surfacearea(r):
    
    surfacearea= math.pi*4*(int(r)**2)
    return(f"La surfacearea de la sphere es:  {str(surfacearea)}")

#volume right_circular_cylinder
@app.route('/figurageometrica/right_circular_cylinder/volume/<r>/<h>', methods=['GET'])
def right_circular_cylinder_volume(r,h):
    
    volume = (int(r)**2)*int(h)*math.pi
    return(f"El volume del right_circular_cylinder es:  {str(volume)}")

#surfacearea right_circular_cylinder
@app.route('/figurageometrica/right_circular_cylinder/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cylinder_surfacearea(r,h):
    
    surfacearea= math.pi*2(int(r)*int(h) + int(r)**2)
    return(f"La surfacearea de la right_circular_cylinder es:  {str(surfacearea)}")

#volume torus
@app.route('/figurageometrica/torus/volume/<r>/<R>', methods=['GET'])
def torus_volume(r,R):
    
    volume = (int(r)**2)*int(R)*(math.pi**2)*2
    return(f"El volume de torus es:  {str(volume)}")

#surfacearea torus
@app.route('/figurageometrica/torus/surfacearea/<r>/<R>', methods=['GET'])
def torus_surfacearea(r,R):
    
    surfacearea= (math.pi**2)*2*(int(r)*int(R))
    return(f"La surfacearea de torus es:  {str(surfacearea)}")

#volume general_cone_or_pyramid
@app.route('/figurageometrica/general_cone_or_pyramid/volume/<a>/<h>', methods=['GET'])
def general_cone_or_pyramid_volume(a,h):
    
    volume = (1/3)*int(a)*int(h)
    return(f"El volume de general_cone_or_pyramid es:  {str(volume)}")

#volume right_circular_cone
@app.route('/figurageometrica/right_circular_cone/volume/<r>/<h>', methods=['GET'])
def right_circular_cone_volume(r,h):
    
    volume = (1/3)*(int(r)**2)*int(h)*math.pi
    return(f"El volume de right_circular_cone es:  {str(volume)}")

#surfacearea right_circular_cone
@app.route('/figurageometrica/right_circular_cone/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cone_surfacearea(r,h):
    
    surfacearea= math.pi*int(r)*math.sqrt(int(r)**2 + int(h)**2) + math.pi*int(r)**2
    return(f"La surfacearea de right_circular_cone es:  {str(surfacearea)}")

#volume frustum_of_a_cone  
@app.route('/figurageometrica/frustum_of_a_cone/volume/<r>/<R>/<h>', methods=['GET'])
def frustum_of_a_cone_volume(r,R,h):
    
    volume = (math.pi/3)((int(r)**2) + int(r)*int(R) + (int(R)**2))*int(h)
    return(f"El volume de frustum_of_a_cone es:  {str(volume)}")

#surface frustum_of_a_cone
@app.route('/figurageometrica/frustum_of_a_cone/surfacearea/<r>/<R>/<h>/<s>', methods=['GET'])
def frustum_of_a_cone_surfacearea(r,R,s):
    
    surfacearea= math.pi(int(s)*(int(R) + int(r)) + int(r)**2 + int(R)**2)
    return(f"La surfacearea de frustum_of_a_cone es:  {str(surfacearea)}")

#volume square_pyramid
@app.route('/figurageometrica/square_pyramid/volume/<s>/<h>', methods=['GET'])
def square_pyramid_volume(s,h):
    
    volume = (1/3)*(int(s)**2)*int(h)
    return(f"El volume de square_pyramid es:  {str(volume)}")

#surfacearea square_pyramid
@app.route('/figurageometrica/square_pyramid/surfacearea/<r>/<R>/<h>/<s>', methods=['GET'])
def square_pyramid_surfacearea(h,s):
    
    surfacearea= int(s)(int(s) + math.sqrt(int(s)**2 + 4*(int(h)**2)))
    return(f"La surfacearea de square_pyramid es:  {str(surfacearea)}")

#volume regular_tetrahedron
@app.route('/figurageometrica/regular_tetrahedron/volume/<s>', methods=['GET'])
def regular_tetrahedron_volume(s):
    
    volume = (1/12)*math.sqrt(2)*(int(s)**3)
    return(f"El volume de regular_tetrahedron es:  {str(volume)}")

#surfacearea regular_tetrahedron
@app.route('/figurageometrica/regular_tetrahedron/surfacearea/<s>', methods=['GET'])
def regular_tetrahedron_surfacearea(s):
   
    surfacearea= math.sqrt(3)*(int(s)**2)
    return(f"La surfacearea de regular_tetrahedron es:  {str(surfacearea)}")
>>>>>>> e83ca76c16bc3b8f225e2e52e13d5159ce498e52

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'),debug=True)
