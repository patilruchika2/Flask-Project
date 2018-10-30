from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required
app = Flask(__name__)
app.config['SECRET_KEY']='HARD TO GUESS STRING'
bootstarp=Bootstrap(app)

class NameForm(Form):
    name=TextField('What is Your Name?',validators=[Required()])

@app.route('/',methods=['GET','POST'])
def index():
    name=None
    form=NameForm()
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=""
    return render_template('index.html',form=form,name=name)


if __name__=="__main__":
    app.run(debug=True)
