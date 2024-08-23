from flask import Flask, render_template, request
import sqlite3, pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods =['GET', 'POST'])
def contactUs():
    if request.method == 'POST':
        # Extract form data
        fname = request.form.get('name')
        fphone = request.form.get('phone')
        femail = request.form.get('email')
        faddress = request.form.get('address')
        fmessage = request.form.get('message')

        conn = sqlite3.connect('ytdatabase.db')
        cur = conn.cursor()
        cur.execute(f'''
                    INSERT INTO CONTACT VALUES(
                    '{fname}', '{fphone}', '{femail}', '{faddress}', '{fmessage}') 
                    ''')
        conn.commit()

        return render_template('thankyou.html')

    else:
        return render_template('contactus.html')


'''@app.route('/thank-you')
def thank_you():
    return render_template('thankyou.html')'''

@app.route('/analytical')
def analytical():
    return render_template('analytical.html')


@app.route('/predict',methods =['GET', 'POST'])
def likepredict():
    if request.method == 'POST':
        views = request.form.get('views')
        dislikes = request.form.get('dislikes')
        comment = request.form.get('comments')
        genre = request.form.get('genre')
        print(views, dislikes, comment, genre)

        with open("model.pickle","rb") as mod:
            model = pickle.load(mod)
        pred = model.predict([[float(views), float(dislikes), float(comment), float(genre)]])

        return render_template('result.html', pred = str(round(pred[0])))
    else:
        return render_template('likepredictor.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5050)





