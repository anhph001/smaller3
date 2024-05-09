from flask import Flask, render_template, session

app = Flask(__name__)

info = {"first_person_name": "", "second_person_name": ""}

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    return render_template('home.html', username="anhpham")

@app.route('/smaller3')
def smaller3():
    return render_template('smaller3.html',
                           first_person_name=info["first_person_name"],
                           second_person_name=info['second_person_name'],
                           first_person_image='img/fpi.jpg'
                           )

@app.route('/faq')
def faq():
    return 'faq'

@app.route('/zodiac')
def zodiac():
    return 'zodiac'

@app.route('/message3')
def message3():
    return 'message3 - under developement'

@app.route('/news')
def news():
    return 'news - under development'

if __name__ == "__main__":
    app.run(debug=True)