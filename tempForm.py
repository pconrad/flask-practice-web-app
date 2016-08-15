from flask.ext.wtf import Form
from wtforms import FloatField
from wtforms.validators import DataRequired

class TempForm(Form):
    fTemp = FloatField('fTemp',validators=[DataRequired()])
