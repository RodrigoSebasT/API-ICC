from flask import Flask, render_template
import math

app = Flask(__name__)

#INICIO DEL CODIGO

#primera pagina
@app.route('/<inicio>')
def mostrar_interfaz(inicio):
    return render_template(inicio)


#volumen del cubo
@app.route('/cubo/volumen/<s>', methods=['GET'])
def cube_volume(s):
    lado = float(s)
    volumen = (lado)**3
    volumen = round(volumen,2)
    
    return """
        <!DOCTYPE html>
        <html lang="es">
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
    lado = float(s)
    surfacearea = 6*((lado)**2)
    surfacearea = round(surfacearea,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del cubo<br><br>El ??rea superficial del cubo es: {}</p>""".format(lado,surfacearea)+"""</div>
        </body>
        </html>"""


#volume general_cone_or_pyramid
@app.route('/conoGeneraloPiramide/volumen/<a>/<h>', methods=['GET'])
def general_cone_or_pyramid_volume(a,h):
    volumen = (1/3)*float(a)*float(h)
    volumen = round(volumen,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""A = {}<br>h = {}<br><br>Donde:<br>A: ??rea de la base del cono o pir??mide general<br>h: altura de la pir??mide o cono general<br><br>El volumen del cono o pir??mide general es: {}</p>""".format(float(a),float(h),volumen)+"""</div>
        </body>
        </html>"""



#volume rectangular_solid
@app.route('/solidoRectangular/volumen/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_volume(l,w,h):
    volumen = float(l)*float(w)*float(h)
    volumen = round(volumen,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""a = {}<br>w = {}<br>h = {}<br><br>Donde:<br>a: largo del s??lido rectangular<br>w: ancho del s??lido rectangular<br>h: altura del s??lido rectangular<br><br>El volumen del s??lido rectangular es: {}</p>""".format(float(l),float(w),float(h),volumen)+"""</div>
        </body>
        </html>"""








    #return(f"El volumen de rectangular_solid es:  {str(volume)}")

#surfacearea rectangular_solid
@app.route('/solidoRectangular/surfacearea/<l>/<w>/<h>', methods=['GET'])
def rectangular_solid_surfacearea(l,w,h):
    surfacearea = 2*(float(l)*float(w) + float(h)*float(l) + float(w)*float(h))
    surfacearea = round(surfacearea,2)
    return """
                <!DOCTYPE html>
            <html lang="es">
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
                    <p class="title">"""+"""a = {}<br>w = {}<br>h = {}<br><br>Donde:<br>a: largo del s??lido rectangular<br>w: ancho del s??lido rectangular<br>h: altura del s??lido rectangular<br><br>El ??rea superficial del s??lido rectangular es: {}</p>""".format(float(l),float(w),float(h),surfacearea)+"""</div>
            </body>
            </html>"""



#volume right_circular_cone
@app.route('/conoCircularRecto/volumen/<r>/<h>', methods=['GET'])
def right_circular_cone_volume(r,h):
    volumen = (1/3)*((float(r))**2)*float(h)*(math.pi)
    volumen = round(volumen,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio del cono circular recto<br>h: altura del cono circular recto<br><br>El volumen del cono circular recto es: {}</p>""".format(float(r),float(h),volumen)+"""</div>
        </body>
        </html>"""












    #return(f"El volume de right_circular_cone es:  {str(volume)}")





#surfacearea right_circular_cone
@app.route('/conoCircularRecto/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cone_surfacearea(r,h):
    surfacearea= ((math.pi)*(float(r))*(math.sqrt(((float(r))**2) + ((float(h))**2)))) + (math.pi*((float(r))**2))
    surfacearea = round(surfacearea,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio del cono circular recto<br>h: altura del cono circular recto<br><br>El ??rea superficial del cono circular recto es: {}</p>""".format(float(r),float(h),surfacearea)+"""</div>
        </body>
        </html>"""




#volume sphere
@app.route('/esfera/volumen/<r>', methods=['GET'])
def sphere_volume(r):
    volumen = ((float(r))**3)*(4/3)*(math.pi)
    volumen = round(volumen,2)
    return """
            <!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br><br>Donde:<br>r: radio de la esfera<br><br>El volumen de la esfera es: {}</p>""".format(float(r),volumen)+"""</div>
        </body>
        </html>"""















    #return(f"El volume de la sphere es:  {str(volume)}")

#surfacearea sphere
@app.route('/esfera/surfacearea/<r>', methods=['GET'])
def sphere_surfacearea(r):
    surfacearea= (math.pi)*4*((float(r))**2)
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br><br>Donde:<br>r: radio de la esfera<br><br>El ??rea superficial de la esfera es: {}</p>""".format(float(r),surfacearea)+"""</div>
        </body>
        </html>"""




















    #return(f"La surfacearea de la sphere es:  {str(surfacearea)}")











    #return(f"La surfacearea de right_circular_cone es:  {str(surfacearea)}")




#volume frustum_of_a_cone  
@app.route('/troncoDeCono/volumen/<r>/<R>/<h>', methods=['GET'])
def frustum_of_a_cone_volume(r,R,h):
    volumen = ((math.pi)/3)*(((float(r))**2) + ((float(r))*(float(R))) + ((float(R))**2))*(float(h))
    volumen = round(volumen,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r(2) = {}<br>r(1) = {}<br>h = {}<br><br>Donde:<br>r(1): radio de la base superior<br>r(2): radio de la base inferior<br>h: altura del tronco de cono<br><br>El volumen del tronco de cono es: {}</p>""".format(float(r),float(R),float(h),volumen)+"""</div>
        </body>
        </html>"""






    #return(f"El volume de frustum_of_a_cone es:  {str(volume)}")




#surface frustum_of_a_cone
@app.route('/troncoDeCono/surfacearea/<r>/<R>/<s>', methods=['GET'])
def frustum_of_a_cone_surfacearea(r,R,s):
    surfacearea= math.pi*((float(s)*(float(R) + float(r))) + ((float(r))**2) + ((float(R))**2))
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r(2) = {}<br>r(1) = {}<br>s = {}<br><br>Donde:<br>r(1): radio de la base superior<br>r(2): radio de la base inferior<br>s: longitud del lado lateral del tronco de cono<br><br>El ??rea superficial del tronco de cono es: {}</p>""".format(float(r),float(R),float(s),surfacearea)+"""</div>
        </body>
        </html>"""







#volume right_circular_cylinder
@app.route('/cilindroCircularRecto/volumen/<r>/<h>', methods=['GET'])
def right_circular_cylinder_volume(r,h):
    volumen = ((float(r))**2)*(float(h))*(math.pi)
    volumen = round(volumen,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio de la base del cilindro circular recto<br>h: altura del cilindro circular recto<br><br>El volumen del cilindro circular recto es: {}</p>""".format(float(r),float(h),volumen)+"""</div>
        </body>
        </html>"""








#surfacearea right_circular_cylinder
@app.route('/cilindroCircularRecto/surfacearea/<r>/<h>', methods=['GET'])
def right_circular_cylinder_surfacearea(r,h):
    surfacearea= (math.pi)*2*((float(r)*float(h)) + ((float(r))**2)) 
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>h = {}<br><br>Donde:<br>r: radio de la base del cilindro circular recto<br>h: altura del cilindro circular recto<br><br>El ??rea superficial del cilindro circular recto es: {}</p>""".format(float(r),float(h),surfacearea)+"""</div>
        </body>
        </html>"""





#volume square_pyramid
@app.route('/piramideCuadrangular/volumen/<s>/<h>', methods=['GET'])
def square_pyramid_volume(s,h):
    volumen = (1/3)*((float(s))**2)*(float(h))
    volumen = round(volumen,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""l = {}<br>h = {}<br><br>Donde:<br>l: longitud del lado de la base de la pir??mide<br>h: altura de la pir??mide<br><br>El volumen de la pir??mide cuadrangular es: {}</p>""".format(float(s),float(h),volumen)+"""</div>
        </body>
        </html>"""




#surfacearea square_pyramid
@app.route('/piramideCuadrangular/surfacearea/<s>/<h>', methods=['GET'])
def square_pyramid_surfacearea(h,s):
    surfacearea= (float(s))*((float(s)) + (math.sqrt(((float(s))**2) + (4*((float(h))**2)))))
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""l = {}<br>h = {}<br><br>Donde:<br>l: longitud del lado de la base de la pir??mide<br>h: altura de la pir??mide<br><br>El ??rea superficial de la pir??mide cuadrangular es: {}</p>""".format(float(s),float(h),surfacearea)+"""</div>
        </body>
        </html>"""






#volume torus
@app.route('/toroide/volumen/<r>/<R>', methods=['GET'])
def torus_volumen(r,R):
    volumen = ((float(r))**2)*(float(R))*((math.pi)**2)*2
    volumen = round(volumen,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>R = {}<br><br>Donde:<br>r: radio del tubo<br>R: radio del toroide<br><br>El volumen del toroide es: {}</p>""".format(float(r),float(R),volumen)+"""</div>
        </body>
        </html>"""








#surfacearea torus
@app.route('/toroide/surfacearea/<r>/<R>', methods=['GET'])
def torus_surfacearea(r,R):
    surfacearea= ((math.pi)**2)*4*(float(r))*(float(R))
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""r = {}<br>R = {}<br><br>Donde:<br>r: radio del tubo<br>R: radio del toroide<br><br>El ??rea superficial del toroide es: {}</p>""".format(float(r),float(R),surfacearea)+"""</div>
        </body>
        </html>"""





#volume regular_tetrahedron
@app.route('/tetraedroRegular/volumen/<s>', methods=['GET'])
def regular_tetrahedron_volume(s):
    volumen = (1/12)*(math.sqrt(2))*((float(s))**3)
    volumen = round(volumen,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del tetraedro regular<br><br>El volumen del tetraedro regular es: {}</p>""".format(float(s),volumen)+"""</div>
        </body>
        </html>"""




#surfacearea regular_tetrahedron
@app.route('/tetraedroRegular/surfacearea/<s>', methods=['GET'])
def regular_tetrahedron_surfacearea(s):
    surfacearea= (math.sqrt(3))*((float(s))**2)
    surfacearea = round(surfacearea,2)
    return """<!DOCTYPE html>
        <html lang="es">
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
                <p class="title">"""+"""s = {}<br><br>Donde:<br>s: lado del tetraedro regular<br><br>El ??rea superficial del tetraedro regular es: {}</p>""".format(float(s),surfacearea)+"""</div>
        </body>
        </html>"""





if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
