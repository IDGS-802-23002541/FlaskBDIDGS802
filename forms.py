from wtforms import Form
from wtforms import StringField, IntegerField, validators

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