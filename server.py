from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

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

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
