from flask import render_template
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route('/index')
def index():
    user = {'username': 'FreshdaxX'}
    posts = [
        {
            'author': {'username': 'Rob'},
            'body': 'Waiting for new FPV Stuff being delivered!'
        },
        {
            'author': {'username': 'Maria'},
            'body': '<3 FPV!'
        },
        {
            'author': {'username': 'Eugen'},
            'body': 'I am so confused'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/about")
def hello():
    return "About Me"


@app.route("/quadcopter")
def members():
    return "Everything about Quadrocopter"


if __name__ == "__main__":
    app.run(host='127.0.0.1')