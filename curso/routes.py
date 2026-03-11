# Blueprint es para manejarlo como módulos
from . import curso_bp
from flask import Flask, render_template, request, redirect, url_for
from models import db
from models import Curso

import forms


@curso_bp.route("/cursos", methods=['POST', 'GET'])
def index():
	create_form=forms.CursoForm(request.form)
	cursos=Curso.query.all()
	return render_template("cursos/curso.html", form=create_form, cursos=cursos)

@curso_bp.route('/insertar_curso', methods=['GET', 'POST'])
def cursos():
	curso_class=forms.CursoForm(request.form)
	if request.method=='POST':
		curso=Curso(
			id=curso_class.id.data,
            nombre=curso_class.nombre.data,
			   descripcion=curso_class.descripcion.data,
			   maestro_id=curso_class.maestro_id.data)
		db.session.add(curso)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("cursos/insertar_curso.html", form=curso_class)

@curso_bp.route('/detalles_curso', methods=['GET', 'POST'])
def detalles():
	curso_class=forms.CursoForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		nombre=curso1.nombre
		descripcion=curso1.descripcion
		maestro_id=curso1.maestro_id
	return render_template("cursos/detalles_curso.html", nombre=nombre, descripcion=descripcion, maestro_id=maestro_id)

@curso_bp.route('/modificar_curso', methods=['GET', 'POST'])
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
		return redirect(url_for('index'))
	return render_template("cursos/modificar_curso.html", form=curso_class)

@curso_bp.route('/eliminar_curso', methods=['GET', 'POST'])
def eliminar():
	curso_class=forms.CursoForm(request.form)
	if request.method=='GET':
		id=request.args.get('id')
		curso1=db.session.query(Curso).filter(Curso.id==id).first()
		curso_class.id.data=request.args.get('id')
		curso_class.nombre.data=curso1.nombre
		curso_class.descripcion.data=curso1.descripcion
		curso_class.maestro_id.data=curso1.maestro_id
	if request.method=='POST':
		id=request.form.get('id')
		curso1=Curso.query.get_or_404(id)
		db.session.delete(curso1)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("cursos/eliminar_curso.html", form=curso_class)
	