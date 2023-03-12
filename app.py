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

@app.route('/',methods=['GET','POST'])
def index():
    print('Hola')
    print(request.form)
    create_form = forms.UserForm(request.form)
    print(create_form.nombre.data)
    if request.method == 'POST' and create_form.validate():
        print('Hola')
        print(create_form.nombre.data)
        alum = Alumno(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('index.html', form=create_form)

@app.route("/ABCompleto", methods=['GET','POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    #select * form alumnos
    alumnos = Alumno.query.all()
    return render_template('ABCompleto.html', form=create_form, alumnos=alumnos)

@app.route("/modificar",methods=['GET','POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select * from alumnos where id = id
        alumn1 = db.session.query(Alumno).filter(Alumno.id == id).first()
        create_form.id.data = alumn1.id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        return render_template('modificar.html', form=create_form)
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumno).filter(Alumno.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apellidos = create_form.apellidos.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form=create_form)

@app.route("/eliminar",methods=['GET','POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        #select * from alumnos where id = id
        alumn1 = db.session.query(Alumno).filter(Alumno.id == id).first()
        create_form.id.data = alumn1.id
        create_form.nombre.data = alumn1.nombre
        create_form.apellidos.data = alumn1.apellidos
        create_form.email.data = alumn1.email
        return render_template('eliminar.html', form=create_form)
    
    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumno).filter(Alumno.id == id).first()
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html', form=create_form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=3000)