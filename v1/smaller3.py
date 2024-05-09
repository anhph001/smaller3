from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def getDiff(month, day, years):
    # Get month, day, years difference
    mdy = datetime(years, month, day)
    cmdy = datetime.now()
    diffMdy = (cmdy - mdy).days

    # Get years, month, days stage
    yDiff = diffMdy // 365
    rmd = diffMdy % 365
    mDiff, dDiff = divmod(rmd, 30)

    return [yDiff, mDiff, dDiff]

def getZodiac(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return ["Bạch Dương", "♈"]
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return ["Kim Ngưu", "♉"]
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return ["Song Tử", "♊"]
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return ["Cự Giải", "♋"]
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return ["Sư Tử", "♌"]
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return ["Xử Nữ", "♍"]
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return ["Thiên Bình", "♎"]
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return ["Bọ Cạp", "♏"]
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return ["Nhân Mã", "♐"]
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return ["Ma Kết", "♑"]
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return ["Bảo Bình", "♒"]
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return ["Song Ngư", "♓"]
    else:
        return ["Ngày không hợp lệ", ""]

@app.route('/')
def redirect():
    return render_template('redirect.html')

@app.route('/zodiac', methods=['GET', 'POST'])
def zodiac():
    if request.method == 'POST':
        # Assuming you have form fields for month and day in the HTML form
        month = int(request.form['month'])
        day = int(request.form['day'])
        
        zodiac_sign, zodiac_symbol = getZodiac(month, day)
        
        return render_template('result.html', zodiac_sign=zodiac_sign, zodiac_symbol=zodiac_symbol)
    else:
        # If its a GET req, render the form for input
        return render_template('zodiac.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/inlove')
def inlove():
    mdyPassed = getDiff(2, 12, 2024)
    left_img = "/static/img1.jpg"
    right_img = "/static/img2.jpg"
    heart_img = "/static/heart.png"
    return render_template('inlove.html', mpassed=mdyPassed[1], dpassed=mdyPassed[2], ypassed=mdyPassed[0], tram=left_img, anhpham=right_img, heart=heart_img, p1age=13, p2age=14)

if __name__ == '__main__':
    app.run(debug=True)
