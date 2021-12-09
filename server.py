from flask import Flask, render_template
from math import pi
import math

app = Flask(__name__)

#INICIO DEL CODIGO

#volumen del cubo
@app.route('/cubo/volumen/<s>', methods=['GET'])
def cube_volume(s):
    lado = int(s)
    volumen = (lado)**3
    
    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 400px;
                    top:-4px;
                    border-radius: 30px;
                    width: 400px;
                    height: 400px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 30px;
                    font-size: 20px;
                    width: 280px;
                    padding: 15px;
                    left: 30px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cubo.png" alt="">
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del cubo<br><br>El volumen del cubo es: {}</p>""".format(lado,volumen)+"""</div>
        </body>
        </html>"""

#area superficial del cubo
@app.route('/cubo/surfacearea/<s>', methods=['GET'])
def cube_surfacearea(s):
    lado = int(s)
    surfacearea = 6*((lado)**2)
    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 400px;
                    top:-4px;
                    border-radius: 30px;
                    width: 400px;
                    height: 400px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 30px;
                    font-size: 20px;
                    width: 280px;
                    padding: 15px;
                    left: 40px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cubo.png" alt="">
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del cubo<br><br>El área superficial del cubo es: {}</p>""".format(lado,surfacearea)+"""</div>
        </body>
        </html>"""


#volume general_cone_or_pyramid
@app.route('/conoGeneraloPiramide/volumen/<a>/<h>', methods=['GET'])
def general_cone_or_pyramid_volume(a,h):
    volumen = (1/3)*int(a)*int(h)

    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 460px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 300px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 18px;
                    font-size: 20px;
                    width: 380px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cono.png" alt="">
                <p class="title">"""+"""A = {}<br>h = {}<br><br>Donde:<br>A: área de la base del cono o pirámide general<br>h: altura de la pirámide o cono general<br><br>El volumen del cono o pirámide general es: {}</p>""".format(int(a),int(h),volumen)+"""</div>
        </body>
        </html>"""



#volume rectangular_solid
@app.route('/solidoRectangular/volumen/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_volume(l,w,h):
    volumen = int(l)*int(w)*int(h)

    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 300px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/solido.png" alt="">
                <p class="title">"""+"""a = {}<br>w = {}<br>h = {}<br><br>Donde:<br>a: largo del sólido rectangular<br>w: ancho del sólido rectangular<br>h: altura del sólido rectangular<br><br>El volumen del sólido rectangular es: {}</p>""".format(int(l),int(w),int(h),volumen)+"""</div>
        </body>
        </html>"""








    #return(f"El volumen de rectangular_solid es:  {str(volume)}")

#surfacearea rectangular_solid
@app.route('/solidoRectangular/surfacearea/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_surfacearea(l,w,h):
    surfacearea = 2*(int(l)*int(w) + int(h)*int(l) + int(w)*int(h))

    return """
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link rel="stylesheet" href="../css/solidoRectangular.css">
                <style>
                    * {
                        background-color: black;
                        color: white;
                        font-family: 'Roboto', sans-serif;
                    }
                    .container {
                        position: relative;
                    }
                    .container img {
                        position: absolute;
                        left: 440px;
                        top:15px;
                        border-radius: 30px;
                        width: 350px;
                        height: 300px;
                        background-color:white;
                    }
                    .container .title {
                        position: relative;
                        top: 20px;
                        font-size: 20px;
                        width: 360px;
                        padding: 15px;
                        left: 10px;
                        border: 2px solid white;
                        border-radius: 20px;
                        text-align: center;
                    }
                    
                </style>
            </head>

            <body>
                <div class="container">
                    <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/solido.png" alt="">
                    <p class="title">"""+"""a = {}<br>w = {}<br>h = {}<br><br>Donde:<br>a: largo del sólido rectangular<br>w: ancho del sólido rectangular<br>h: altura del sólido rectangular<br><br>El volumen del sólido rectangular es: {}</p>""".format(int(l),int(w),int(h),surfacearea)+"""</div>
            </body>
            </html>"""



#volume right_circular_cone
@app.route('/conoCircularRecto/volumen/<r>/<h>', methods=['GET'])
def right_circular_cone_volume(r,h):
    volumen = (1/3)*((int(r))**2)*int(h)*(math.pi)

    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 300px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/copia.png" alt="">
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio del cono circular recto<br>h: altura del cono circular recto<br><br>El volumen del cono circular recto es: {}</p>""".format(int(r),int(h),volumen)+"""</div>
        </body>
        </html>"""












    #return(f"El volume de right_circular_cone es:  {str(volume)}")





#surfacearea right_circular_cone
@app.route('/conoCircularRecto/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cone_surfacearea(r,h):
    surfacearea= ((math.pi)*(int(r))*(math.sqrt(((int(r))**2) + ((int(h))**2)))) + (math.pi*((int(r))**2))

    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 300px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/copia.png" alt="">
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio del cono circular recto<br>h: altura del cono circular recto<br><br>El área superficial del cono circular recto es: {}</p>""".format(int(r),int(h),surfacearea)+"""</div>
        </body>
        </html>"""




#volume sphere
@app.route('/esfera/volumen/<r>', methods=['GET'])
def sphere_volume(r):
    volumen = ((int(r))**3)*(4/3)*(math.pi)

    return """
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 315px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/esfera.gif" alt="">
                <p class="title">"""+"""r = {}<br><br>Donde:<br>r: radio de la esfera<br><br>El volumen de la esfera es: {}</p>""".format(int(r),volumen)+"""</div>
        </body>
        </html>"""















    #return(f"El volume de la sphere es:  {str(volume)}")

#surfacearea sphere
@app.route('/esfera/surfacearea/<r>', methods=['GET'])
def sphere_surfacearea(r):
    surfacearea= (math.pi)*4*((int(r))**2)

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 315px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/esfera.gif" alt="">
                <p class="title">"""+"""r = {}<br><br>Donde:<br>r: radio de la esfera<br><br>El área superficial de la esfera es: {}</p>""".format(int(r),surfacearea)+"""</div>
        </body>
        </html>"""




















    #return(f"La surfacearea de la sphere es:  {str(surfacearea)}")











    #return(f"La surfacearea de right_circular_cone es:  {str(surfacearea)}")




#volume frustum_of_a_cone  
@app.route('/troncoDeCono/volumen/<r>/<R>/<h>', methods=['GET'])
def frustum_of_a_cone_volume(r,R,h):
    volumen = ((math.pi)/3)*(((int(r))**2) + ((int(r))*(int(R))) + ((int(R))**2))*(int(h))

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 315px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/troncoCono.jpg" alt="">
                <p class="title">"""+"""r(2) = {}<br>r(1) = {}<br>h = {}<br><br>Donde:<br>r(1): radio de la base superior<br>r(2): radio de la base inferior<br>h: altura del tronco de cono<br><br>El volumene del tronco de cono es: {}</p>""".format(int(r),int(R),int(h),volumen)+"""</div>
        </body>
        </html>"""






    #return(f"El volume de frustum_of_a_cone es:  {str(volume)}")




#surface frustum_of_a_cone
@app.route('/troncoDeCono/surfacearea/<r>/<R>/<s>', methods=['GET'])
def frustum_of_a_cone_surfacearea(r,R,s):
    surfacearea= math.pi*((int(s)*(int(R) + int(r))) + ((int(r))**2) + ((int(R))**2))
    
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 315px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/troncoCono.jpg" alt="">
                <p class="title">"""+"""r(2) = {}<br>r(1) = {}<br>s = {}<br><br>Donde:<br>r(1): radio de la base superior<br>r(2): radio de la base inferior<br>s: longitud del lado lateral del tronco de cono<br><br>El volumene del tronco de cono es: {}</p>""".format(int(r),int(R),int(s),surfacearea)+"""</div>
        </body>
        </html>"""







#volume right_circular_cylinder
@app.route('/cilindroCircularRecto/volumen/<r>/<h>', methods=['GET'])
def right_circular_cylinder_volume(r,h):
    volumen = ((int(r))**2)*(int(h))*(math.pi)

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 330px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cilindroo.png" alt="">
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio de la base del cilindro circular recto<br>h: altura del cilindro circular recto<br><br>El volumen del cilindro circular recto es: {}</p>""".format(int(r),int(h),volumen)+"""</div>
        </body>
        </html>"""








#surfacearea right_circular_cylinder
@app.route('/cilindroCircularRecto/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cylinder_surfacearea(r,h):
    surfacearea= (math.pi)*2*((int(r)*int(h)) + ((int(r))**2)) 
    
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 330px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/cilindroo.png" alt="">
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio de la base del cilindro circular recto<br>h: altura del cilindro circular recto<br><br>El área superficial del cilindro circular recto es: {}</p>""".format(int(r),int(h),surfacearea)+"""</div>
        </body>
        </html>"""





#volume square_pyramid
@app.route('/piramideCuadrangular/volumen/<s>/<h>', methods=['GET'])
def square_pyramid_volume(s,h):
    volumen = (1/3)*((int(s))**2)*(int(h))
    
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 330px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/piramideRectangular.png" alt="">
                <p class="title">"""+"""l = {}<br>h = {}<br><br>Donde:<br>l: longitud del lado de la base de la pirámide<br>h: altura de la pirámide<br><br>El volumen de la pirámide cuadrangular es: {}</p>""".format(int(s),int(h),volumen)+"""</div>
        </body>
        </html>"""




#surfacearea square_pyramid
@app.route('/piramideCuadrangular/surfacearea/<s>/<h>', methods=['GET'])
def square_pyramid_surfacearea(h,s):
    surfacearea= (int(s))*((int(s)) + (math.sqrt(((int(s))**2) + (4*((int(h))**2)))))

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 350px;
                    height: 330px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/piramideRectangular.png" alt="">
                <p class="title">"""+"""l = {}<br>h = {}<br><br>Donde:<br>l: longitud del lado de la base de la pirámide<br>h: altura de la pirámide<br><br>El área superficial de la pirámide cuadrangular es: {}</p>""".format(int(s),int(h),surfacearea)+"""</div>
        </body>
        </html>"""






#volume torus
@app.route('/toroide/volumen/<r>/<R>', methods=['GET'])
def torus_volumen(r,R):
    volumen = ((int(r))**2)*(int(R))*((math.pi)**2)*2

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 370px;
                    height: 350px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/toro.png" alt="">
                <p class="title">"""+"""r = {}<br>R = {}<br><br>Donde:<br>r: radio del tubo<br>R: radio del toroide<br><br>El volumen del toroide es: {}</p>""".format(int(r),int(R),volumen)+"""</div>
        </body>
        </html>"""








#surfacearea torus
@app.route('/toroide/surfacearea/<r>/<R>', methods=['GET'])
def torus_surfacearea(r,R):
    surfacearea= ((math.pi)**2)*4*(int(r))*(int(R))

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 440px;
                    top:15px;
                    border-radius: 30px;
                    width: 370px;
                    height: 350px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/toro.png" alt="">
                <p class="title">"""+"""r = {}<br>R = {}<br><br>Donde:<br>r: radio del tubo<br>R: radio del toroide<br><br>El área superficial del toroide es: {}</p>""".format(int(r),int(R),surfacearea)+"""</div>
        </body>
        </html>"""





#volume regular_tetrahedron
@app.route('/tetraedroRegular/volumen/<s>', methods=['GET'])
def regular_tetrahedron_volume(s):
    volumen = (1/12)*(math.sqrt(2))*((int(s))**3)

    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <link rel="stylesheet" href="../css/solidoRectangular.css">
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 445px;
                    top:-8px;
                    border-radius: 30px;
                    width: 370px;
                    height: 350px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/tetraedro.png" alt="">
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del tetraedro regular<br><br>El volumen del tetraedro regular es: {}</p>""".format(int(s),volumen)+"""</div>
        </body>
        </html>"""




#surfacearea regular_tetrahedron
@app.route('/tetraedroregular/surfacearea/<s>', methods=['GET'])
def regular_tetrahedron_surfacearea(s):
    surfacearea= (math.sqrt(3))*((int(s))**2)
    
    return """<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                * {
                    background-color: black;
                    color: white;
                    font-family: 'Roboto', sans-serif;
                }
                .container {
                    position: relative;
                }
                .container img {
                    position: absolute;
                    left: 445px;
                    top:-8px;
                    border-radius: 30px;
                    width: 370px;
                    height: 350px;
                    background-color:white;
                }
                .container .title {
                    position: relative;
                    top: 20px;
                    font-size: 20px;
                    width: 360px;
                    padding: 15px;
                    left: 10px;
                    border: 2px solid white;
                    border-radius: 20px;
                    text-align: center;
                }
                
            </style>
        </head>

        <body>
            <div class="container">
                <img src="https://raw.githubusercontent.com/RodrigoSebasT/API-ICC/main/static/images/tetraedro.png" alt="">
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del tetraedro regular<br><br>El área superficial del tetraedro regular es: {}</p>""".format(int(s),surfacearea)+"""</div>
        </body>
        </html>"""





if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'),debug=True)
