from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, SelectField
from wtforms.validators import DataRequired


class SQLForm(FlaskForm):
    database = SelectField("Database", choices=[("academic", "academic")])
    query = StringField('Natural Language Query', validators=[DataRequired()])
    submit = SubmitField('Evaluate')
