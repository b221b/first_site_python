from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Главная страница')


@app.route('/about')
def about():
    return render_template('about.html', title='О нас')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты')


@app.route('/elements')
def elements():
    return render_template('elements.html', title='Элементы')


@app.route('/generic')
def generic():
    return render_template('generic.html', title='Generic')


if __name__ == '__main__':
    app.run(debug=True)
