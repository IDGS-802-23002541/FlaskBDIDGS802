# Blueprint es para manejarlo como módulos
from . import alumnos_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Alumnos

import forms


@alumnos_bp.route("/alumnos", methods=['POST', 'GET'])
def index():
	create_form=forms.UserForm(request.form)
	alumno=Alumnos.query.all()
	return render_template("alumnos/alumnos.html", form=create_form, alumno=alumno)

@alumnos_bp.route('/insertar', methods=['GET', 'POST'])
def alumnos():
	alumno_class=forms.UserForm(request.form)
	if request.method=='POST':
		alum=Alumnos(nombre=alumno_class.nombre.data,
			   apellidos=alumno_class.apaterno.data,
			   email=alumno_class.email.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('alumnos.alumnos'))
	return render_template("alumnos/insertar.html", form=alumno_class)

@alumnos_bp.route('/detalles', methods=['GET', 'POST'])
def detalles():
	alumno_class=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumn1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		nombre=alumn1.nombre
		apellidos=alumn1.apellidos
		email=alumn1.email
		telefono=alumn1.telefono
		cursos=alumn1.cursos
	return render_template("alumnos/detalles.html", nombre=nombre, apellidos=apellidos, email=email, telefono=telefono, cursos=cursos)

@alumnos_bp.route('/modificar', methods=['GET', 'POST'])
def modificar():
	alumno_class=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumn1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumno_class.id.data=request.args.get('id')
		alumno_class.nombre.data=alumn1.nombre
		alumno_class.apellidos.data=alumn1.apellidos
		alumno_class.email.data=alumn1.email
		alumno_class.telefono.data=alumn1.telefono
	if request.method=='POST':
		id=alumno_class.id.data
		alumn=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumn.id=id
		alumn.nombre=str.rstrip(alumno_class.nombre.data)
		alumn.apellidos=alumno_class.apellidos.data
		alumn.email=alumno_class.email.data
		alumn.telefono=alumno_class.telefono.data
		db.session.add(alumn)
		db.session.commit()
		return redirect(url_for('alumnos.alumnos'))
	return render_template("alumnos/modificar.html", form=alumno_class)

@alumnos_bp.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
	alumno_class=forms.UserForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		alumn1=db.session.query(Alumnos).filter(Alumnos.id==id).first()
		alumno_class.id.data=request.args.get('id')
		alumno_class.nombre.data=alumn1.nombre
		alumno_class.apellidos.data=alumn1.apellidos
		alumno_class.email.data=alumn1.email
		alumno_class.telefono.data=alumn1.telefono
	if request.method=='POST':
		id=request.form.get('id')
		alumn=Alumnos.query.get_or_404(id)
		db.session.delete(alumn)
		db.session.commit()
		return redirect(url_for('alumnos.alumnos'))
	return render_template("alumnos/eliminar.html", form=alumno_class)
	