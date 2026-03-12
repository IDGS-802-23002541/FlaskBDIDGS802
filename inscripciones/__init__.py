from flask import Blueprint

insc_bp=Blueprint(
	'inscripciones',
	 __name__,
	 template_folder='templates')

from . import routes