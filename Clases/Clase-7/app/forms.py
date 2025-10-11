from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    title = StringField("Nueva tarea", validators=[DataRequired()])
    submit = SubmitField("Agregar")
