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
	cursos=Curso.query.all()
	return render_template("inscripciones/inscrip.html", form=create_form, cursos=cursos)

@insc_bp.route('/insertar_inscripciones', methods=['GET', 'POST'])
def insertar():
	curso_class=forms.CursoForm(request.form)
	if request.method=='POST':
		curso=Curso(
			id=curso_class.id.data,
            nombre=curso_class.nombre.data,
			descripcion=curso_class.descripcion.data,
			maestro_id=curso_class.maestro_id.data
			
		)
		db.session.add(curso)
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	maestros = Maestros.query.all()
	return render_template("inscripciones/insertar_inscrip.html", form=curso_class, maestros=maestros)

@insc_bp.route('/detalles_inscripciones', methods=['GET', 'POST'])
def detalles():
	curso_class=forms.CursoForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		nombre=curso1.nombre
		descripcion=curso1.descripcion
		maestro_id=curso1.maestro.nombre + " " + curso1.maestro.apellidos
	return render_template("inscripciones/detalles_inscrip.html", nombre=nombre, descripcion=descripcion, maestro_id=maestro_id)

@insc_bp.route('/modificar_inscripciones', methods=['GET', 'POST'])
def modificar():
	curso_class=forms.CursoForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		curso_class.id.data=request.args.get('id')
		curso_class.nombre.data=curso1.nombre
		curso_class.descripcion.data=curso1.descripcion
		curso_class.maestro_id.data=curso1.maestro_id
	if request.method=='POST':
		id=curso_class.id.data
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		curso1.id=id
		curso1.nombre=str.rstrip(curso_class.nombre.data)
		curso1.descripcion=curso_class.descripcion.data
		curso1.maestro_id=curso_class.maestro_id.data
		db.session.add(curso1)
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	return render_template("inscripciones/modificar_inscrip.html", form=curso_class)

@insc_bp.route('/eliminar_inscripciones', methods=['GET', 'POST'])
def eliminar():
	curso_class=forms.CursoForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		curso_class.id.data=request.args.get('id')
		curso_class.nombre.data=curso1.nombre
		curso_class.descripcion.data=curso1.descripcion
		curso_class.maestro_id.data=curso1.maestro.nombre + curso1.maestro.apellidos
	if request.method=='POST':
		id=request.form.get('id')
		curso1=Curso.query.get_or_404(id)
		db.session.delete(curso1)
		db.session.commit()
		return redirect(url_for('inscripciones.inscripciones'))
	return render_template("inscripciones/eliminar_inscrip.html", form=curso_class)
	