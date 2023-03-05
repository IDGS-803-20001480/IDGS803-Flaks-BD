from flask import Flask, redirect, render_template
from flask import request
from flask import url_for
import forms

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from model import db
from model import Alumno

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf= CSRFProtect(app)

@app.route('/')
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        print(create_form.nombre.data)
        alum = Alumno(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form=create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)