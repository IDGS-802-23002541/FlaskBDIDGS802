from wtforms import Form
from wtforms import StringField, IntegerField, validators, DateField

class UserForm(Form):
    id=StringField('id', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apellidos=StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido")
    ])
    email=StringField('Email', [
        validators.Email(message="Ingrese un correo válido")
    ])
    telefono=StringField('Telefono', [
        validators.DataRequired(message="Ingrese un teléfono válido")
    ])

class MaestrosForm(Form):
    matricula=StringField('matricula', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese una matricula válida")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apellidos=StringField('Apellidos', [
        validators.DataRequired(message="El campo es requerido")
    ])
    especialidad=StringField('Especialidad', [
        validators.DataRequired(message="Ingrese una especialidad válida")
    ])
    email=StringField('Email', [
        validators.Email(message="Ingrese un correo válido")
    ])
    
class CursoForm(Form):
    id=StringField('id', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    descripcion=StringField('Descripción', [
        validators.DataRequired(message="El campo es requerido")
    ])
    maestro_id=StringField('Maestro', [
        validators.DataRequired(message="El campo es requerido")
    ])

class InscripcionForm(Form):
    id=StringField('id', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    curso_id=StringField('Curso', [
        validators.DataRequired(message="El campo es requerido")
    ])
    alumno_id=StringField('Alumno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    fecha_inscripcion=DateField('Fecha inscripción', [
        validators.DataRequired(message="El campo es requerido")
    ])
