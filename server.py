from flask import Flask, render_template
app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

#no editar nada de arriba
@app.route('/<figurageometrica>/<opcion>/', methods=['GET'])
#figura geometrica = cubo,piramide...
#opcion = volumen o surfacearea
def calcularOpcion(opcion,figurageometrica):
    if opcion.lower()=='volumen':
        pass

    elif opcion.lower()=='surfacearea':
        pass



#no editar nada de abajo
if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
