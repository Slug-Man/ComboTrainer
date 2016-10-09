from flask import Flask, render_template, request, flash, redirect
from flask_wtf.csrf import CsrfProtect

from flopeval.flopevaluator import FlopEvaluator
from flopeval.card import Card
from flopeval.deck import Deck
from flopeval.constants import HANDS, HANDS_VALUE
from itertools import combinations

from forms import ComboForm

app = Flask(__name__)
CsrfProtect(app)


@app.route('/combo')
def combo():
    form = ComboForm()
    return render_template('form2.html',  form=form, hands=HANDS)


@app.route('/comboresults', methods=['POST'])
def combo_results():
    form = ComboForm()
    if form.validate():
        return render_template('results2.html', results=field_values_to_list(form['combos']), hands=HANDS)
    return 'error'


def field_values_to_list(fields):
    l = []
    for f in fields:
        if f.data is None:
            l.append(0)
        else:
            l.append(f.data)
    return l


@app.route('/')
def hello_world():
    return render_template('form.html', hands=HANDS)


@app.route('/results', methods=['POST'])
def results():
    f1 = Card.new(request.form['flop1'])
    f2 = Card.new(request.form['flop2'])
    f3 = Card.new(request.form['flop3'])
    count = {}
    for h in HANDS_VALUE.values():
        count[h] = 0
    for c1, c2 in combinations(Deck(remove=[f1, f2, f3]).cards, 2):
        count[FlopEvaluator.evaluate([f1, f2, f3], [c1, c2])] += 1
    string = ''
    for h in HANDS:
        string += "<b>%s</b><br>Given: %s<br>Actual: %s<br>" % (h,
                                                                request.form[str(HANDS_VALUE[h])],
                                                                count[HANDS_VALUE[h]])
    return string

if __name__ == '__main__':
    app.secret_key = 'laskdjflksasldkftestplsreplace'
    app.run(
        host="127.0.0.1",
        port=int("5555")
    )
