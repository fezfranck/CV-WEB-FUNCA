from flask import Flask, render_template
import os
from datetime import datetime

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
            if filename.endswith('.txt'):
                # Extraer información del archivo
                filepath = os.path.join(articulos_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                    
                # Formato simple: primera línea = título, segunda = fecha, resto = contenido
                titulo = lines[0].strip() if lines else "Sin título"
                fecha = lines[1].strip() if len(lines) > 1 else datetime.now().strftime("%d/%m/%Y")
                contenido = ''.join(lines[2:]) if len(lines) > 2 else "Contenido no disponible"
                
                # Reemplazar saltos de línea por <br> para formato básico
                contenido = contenido.replace('\n', '<br>')
                
                articulos.append({
                    'titulo': titulo,
                    'fecha': fecha,
                    'contenido': contenido,
                    'archivo': filename
                })
    
    # Ordenar artículos por fecha (más reciente primero)
    articulos.sort(key=lambda x: x['fecha'], reverse=True)
    
    return render_template('articulos.html', articulos=articulos)

if __name__ == '__main__':
    app.run(debug=True)
