from wtforms import FieldList, IntegerField, validators
from flask_wtf import FlaskForm

from flopeval.constants import HANDS


class ComboForm(FlaskForm):
    combos = FieldList(IntegerField('combos', [validators.NumberRange(), validators.Optional(True)]),
                       min_entries=len(HANDS),
                       max_entries=len(HANDS))
