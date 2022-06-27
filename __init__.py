from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

model = None

with open('model.pkl', 'rb') as pickle_file:
    model = pickle.load(pickle_file)

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def first():
    if request.method == 'POST':
        return redirect(url_for('second'))
    else:
        return render_template('page1.html')

@app.route('/heart_condition/', methods = ['GET', 'POST'])
def second():
    if request.method == 'GET':
        return render_template('page2.html')
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = str(request.form['sex'])
        chestpaintype = str(request.form['chestpaintype'])
        restingbp = int(request.form['restingbp'])
        cholesterol = int(request.form['cholesterol'])
        fastingbs = int(request.form['fastingbs'])
        restecg = str(request.form['restecg'])
        maxhr = int(request.form['maxhr'])
        exerciseangina = str(request.form['exerciseangina'])
        oldpeak = int(request.form['oldpeak'])
        stslope = str(request.form['stslope'])

        heartfailure = [age, sex, chestpaintype, restingbp, cholesterol, fastingbs, restecg, maxhr, exerciseangina, oldpeak, stslope]
        df = pd.DataFrame([heartfailure], columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope'])
        pred = model.predict(df)

        return render_template('page3.html', data=pred)


@app.route('/result/', methods = ['GET', 'POST'])
def third():
    if request.method == 'POST':
        return redirect(url_for('second'))
    return render_template('page3.html')


if __name__ == "__main__":
    app.run(debug = True)