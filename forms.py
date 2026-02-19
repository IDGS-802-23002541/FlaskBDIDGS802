from wtforms import Form
from wtforms import StringField, IntegerField, validators

class UserForm(Form):
    id=IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor válido")
    ])
    nombre=StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno=StringField('Apaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno=StringField('Amaterno', [
        validators.DataRequired(message="El campo es requerido")
    ])
    correo=StringField('Correo', [
        validators.Email(message="Ingrese un correo válido")
    ])