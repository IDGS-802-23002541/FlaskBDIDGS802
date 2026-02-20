from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms

from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
csrf=CSRFProtect()

@app.route("/", methods=['POST', 'GET'])
@app.route("/index")
def index():
	create_form=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("index.html", form=create_form, alumno=alumno)

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
	alumno_class=forms.UserForm(request.form)
	if request.method=='POST':
		alum=Alumnos(nombre=alumno_class.nombre.data,
			   apaterno=alumno_class.apaterno.data,
			   email=alumno_class.email.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("Alumnos.html", form=alumno_class)

@app.route('/detalles', methods=['GET', 'POST'])
def detalles():
	alumno_class=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumn1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		nombre=alumn1.nombre
		apaterno=alumn1.apaterno
		email=alumn1.email
	return render_template("detalles.html", nombre=nombre, apaterno=apaterno, email=email)

@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
	alumno_class=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumn1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumno_class.id.data=request.args.get('id')
		alumno_class.nombre.data=alumn1.nombre
		alumno_class.apaterno.data=alumn1.apaterno
		alumno_class.email.data=alumn1.email
	if request.method=='POST':
		id=alumno_class.id.data
		alumn=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumn.id=id
		alumn.nombre=str.rstrip(alumno_class.nombre.data)
		alumn.apaterno=alumno_class.apaterno.data
		alumn.email=alumno_class.email.data
		db.session.add(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html", form=alumno_class)
	
@app.errorhandler(404)
def page_not_fount(e):
	return render_template("404.html"), 404

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)

