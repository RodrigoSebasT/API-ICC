from flask import Flask, render_template, flash, url_for
from math import pi

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

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

#no editar nada de abajo
if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'),debug=True)
