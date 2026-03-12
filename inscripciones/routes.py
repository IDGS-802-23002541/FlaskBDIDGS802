# Blueprint es para manejarlo como módulos
from . import insc_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Inscripcion
from models import Curso
from models import Alumnos

import forms


@insc_bp.route("/inscripciones", methods=['POST', 'GET'])
def inscripciones():
	create_form=forms.InscripcionForm(request.form)
	insc=db.session.query(
		Inscripcion,
		Curso,
		Alumnos
	).join(
		Alumnos, Inscripcion.alumno_id == Alumnos.id
	).join(
		Curso, Inscripcion.curso_id == Curso.id
	).all()
	return render_template("inscripciones/inscrip.html", form=create_form, insc=insc)

@insc_bp.route('/insertar_inscripciones', methods=['GET', 'POST'])
def insertar():
	inscripciones_class=forms.InscripcionForm(request.form)
	alumnos = Alumnos.query.all()
	cursos = Curso.query.all()
	if request.method=='POST':
		insc=Inscripcion(
			alumno_id=inscripciones_class.alumno_id.data,
			curso_id=inscripciones_class.curso_id.data
		)
		db.session.add(insc)
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	return render_template("inscripciones/insertar_inscrip.html", form=inscripciones_class, alumnos=alumnos, cursos=cursos)

@insc_bp.route('/detalles_inscripciones', methods=['GET', 'POST'])
def detalles():
	inscripciones_class=forms.InscripcionForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		insc=db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
	return render_template("inscripciones/detalles_inscrip.html", insc=insc)

@insc_bp.route('/modificar_inscripciones', methods=['GET', 'POST'])
def modificar():
	inscripciones_class=forms.InscripcionForm(request.form)
	alumnos=Alumnos.query.all()
	cursos=Curso.query.all()
	if request.method=='GET':
		id=request.args.get('id')
		insc=db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		inscripciones_class.id.data=request.args.get('id')
		inscripciones_class.curso_id.data=insc.curso_id
		inscripciones_class.alumno_id.data=insc.alumno_id
		inscripciones_class.fecha_inscripcion.data=insc.fecha_inscripcion
	if request.method=='POST':
		id=inscripciones_class.id.data
		insc=db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		insc.alumno_id = inscripciones_class.alumno_id.data
		insc.curso_id = inscripciones_class.curso_id.data
		insc.fecha_inscripcion = inscripciones_class.fecha_inscripcion.data
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	return render_template("inscripciones/modificar_inscrip.html", form=inscripciones_class, insc=insc, alumnos=alumnos, cursos=cursos)

@insc_bp.route('/eliminar_inscripciones', methods=['GET', 'POST'])
def eliminar():
	inscripciones_class=forms.InscripcionForm(request.form)
	alumnos=Alumnos.query.all()
	cursos=Curso.query.all()
	if request.method=='GET':
		id=request.args.get('id')
		insc=db.session.query(Inscripcion).filter(Inscripcion.id==id).first()
		inscripciones_class.id.data=request.args.get('id')
		inscripciones_class.curso_id.data=insc.curso_id
		inscripciones_class.alumno_id.data=insc.alumno_id
		inscripciones_class.fecha_inscripcion.data=insc.fecha_inscripcion
	if request.method=='POST':
		id=inscripciones_class.id.data
		insc=Inscripcion.query.get_or_404(id)
		db.session.delete(insc)
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	return render_template("inscripciones/eliminar_inscrip.html", form=inscripciones_class, insc=insc, alumnos=alumnos, cursos=cursos)
	