from flask import Flask, request, jsonify
from flask_wtf import FlaskForm as Form
from wtforms import StringField
from wtforms.validators import DataRequired, AnyOf
from werkzeug.datastructures import MultiDict

app = Flask(__name__)
app.testing = True


class NewWidget(Form):
    name = StringField('Name', validators=[DataRequired(), AnyOf(['eep',
                                                                  'oop'])])


@app.before_request
def before_request():
    if request.is_json:
        request.form = MultiDict(request.get_json())


@app.route('/api/widgets', methods=['POST'])
def widgets():
    form = NewWidget(request.form, meta={'csrf': None})
    if form.validate_on_submit():
        return jsonify(message="Thanks for the widget")
    return jsonify(form.errors)


if __name__ == "__main__":
    app.run()
