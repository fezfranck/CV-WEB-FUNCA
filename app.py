from flask import Flask, render_template
import os

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
    # Obtener lista de artículos disponibles
    articulos_dir = 'static/articulos'
    articulos = []
    
    if os.path.exists(articulos_dir):
        for filename in os.listdir(articulos_dir):
            if filename.endswith('.html'):
                # Extraer información del archivo
                filepath = os.path.join(articulos_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    contenido = file.read()
                
                # Extraer título y fecha del contenido (puedes usar metadatos)
                # O puedes usar el nombre del archivo para el título
                titulo = filename.replace('.html', '').replace('_', ' ').title()
                fecha = "Fecha no disponible"  # Puedes agregar metadatos al archivo
                
                articulos.append({
                    'titulo': titulo,
                    'fecha': fecha,
                    'contenido': contenido,
                    'archivo': filename
                })
    
    return render_template('articulos.html', articulos=articulos)
                })
    
    # Ordenar artículos por fecha (más reciente primero)
    articulos.sort(key=lambda x: x['titulo'])  # O por fecha si la agregas
    
    return render_template('articulos.html', articulos=articulos)

if __name__ == '__main__':
    app.run(debug=True)
