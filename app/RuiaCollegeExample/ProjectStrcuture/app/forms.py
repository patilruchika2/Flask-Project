from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class NameForm(Form):
    name=TextField('What is Your Name?',validators=[Required()])

