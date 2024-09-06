from flask import Flask,render_template,url_for,redirect,request
import numpy as np
import pickle
import json
import requests

app = Flask(__name__)
model=pickle.load(open('Ensemble.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        city = request.form['city']
        country = request.form['country']
        api_key = "5d347f525478241d9959f68c70150849"

        weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=metric')

        weather_data = weather_url.json()


        temp = round(weather_data['main']['temp'])
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        #Rainfall = weather_data['rain']['1h']

        return render_template("index.html", temp=temp, humidity=humidity, wind_speed=wind_speed, city=city)

    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict',methods=['POST'])
def predict():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    arr=np.array([data1,data2,data3,data4,data5,data6,data7])
    single_pred = np.array(arr).reshape(1,-1)
    predictions = model.predict(single_pred)
    prediction_text =predictions[0]

    return render_template('predict.html', prediction_text1=prediction_text.title())

    #if (predictions == ['rice']): 

        #return render_template('agri.html')

    #else:

    

@app.route('/seed')
def seed():
    return render_template('seed.html')

@app.route('/agri')
def agri():
    return render_template('agri.html') 

@app.route('/soillab')
def soillab():
    return render_template('soillab.html') 

@app.route('/soillab/anantapur')
def anantapur():
    return render_template('anantapur.html')

@app.route('/soillab/chitoor')
def chitoor():
    return render_template('chitoor.html') 

@app.route('/soillab/eastGodavari')
def eastGodavari():
    return render_template('eastGodavari.html')

@app.route('/soillab/guntur')
def guntur():
    return render_template('guntur.html')



@app.route('/soillab/krishna')
def krishna():
    return render_template('krishna.html')

@app.route('/soillab/kurnool')
def kurnool():
    return render_template('kurnool.html')

@app.route('/soillab/prakasam')
def prakasam():
    return render_template('prakasam.html')

@app.route('/soillab/spsrnellore')
def spsrnellore():
    return render_template('spsrnellore.html')

@app.route('/soillab/srikakulam')
def srikakulam():
    return render_template('srikakulam.html')

@app.route('/soillab/Visakhapattanam')
def Visakhapattanam():
    return render_template('Visakhapattanam.html')

@app.route('/soillab/vizianagaram')
def vizianagaram():
    return render_template('vizianagaram.html')

@app.route('/soillab/westgodawari')
def westgodawari():
    return render_template('westgodawari.html')

@app.route('/soillab/ysr')
def ysr():
    return render_template('ysr.html') 



if __name__ == '__main__':
    app.debug=True
    app.run()