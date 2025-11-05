from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/educacion')
def educacion():
    return render_template('educacion.html')

@app.route('/experiencias')
def experiencias():
    return render_template('experiencias.html')

@app.route('/quien_soy')
def quien_soy():
    return render_template('quiensoy.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/articulos')
def articulos():
    # CON EL NUEVO SISTEMA, SOLO RENDERIZAMOS LA PLANTILLA
    # JavaScript se encargará de cargar los artículos automáticamente
    return render_template('articulos.html')

if __name__ == '__main__':
    app.run(debug=True)
