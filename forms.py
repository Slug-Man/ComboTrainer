from wtforms import FieldList, IntegerField, StringField, validators
from flask_wtf import FlaskForm

from flopeval.constants import HANDS


class ComboForm(FlaskForm):
    combos = FieldList(IntegerField('combos', [validators.NumberRange(), validators.Optional(True)]),
                       min_entries=len(HANDS),
                       max_entries=len(HANDS))

    flop1 = StringField('flop1', [validators.Optional(True)])
    flop2 = StringField('flop2', [validators.Optional(True)])
    flop3 = StringField('flop3', [validators.Optional(True)])

    range = StringField('range', [validators.Optional(True)])