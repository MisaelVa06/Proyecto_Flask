from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        correo = request.form.get('correo')
        mensaje = request.form.get('mensaje')
        
        if not nombre or not correo or not mensaje:
             error = "Por favor completa todos los campos."
             return render_template('contact.html', error=error)
    
        return render_template('response.html', nombre=nombre)
   
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(debug=True)
