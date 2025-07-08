from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///contactos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contacto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(120), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Contacto {self.nombre}>'


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
        
        nuevo_contacto = Contacto(nombre=nombre, correo=correo, mensaje=mensaje)
        db.session.add(nuevo_contacto)
        db.session.commit()

        return render_template('response.html', nombre=nombre)
        

    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True)
