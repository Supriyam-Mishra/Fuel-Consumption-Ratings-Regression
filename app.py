from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('decisiontree_regressor.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    # vehicle_class=0
    if request.method == 'POST':
        vehicle_class = request.form['vehicle_class']
        if (vehicle_class=='Compact'):
            vehicle_class=0
        elif (vehicle_class=='Full_size'):
            vehicle_class=1
        elif (vehicle_class=='Mid_size'):
            vehicle_class=2
        elif (vehicle_class=='Minicompact'):
            vehicle_class=3
        elif (vehicle_class=='Minivan'):
            vehicle_class=4
        elif (vehicle_class=='pt_small'):
            vehicle_class=5
        elif (vehicle_class=='pt_std'):
            vehicle_class=6
        elif (vehicle_class=='suv_small'):
            vehicle_class=7
        elif (vehicle_class=='suv_standard'):
            vehicle_class=8
        elif (vehicle_class=='spv'):
            vehicle_class=9
        elif (vehicle_class=='swms'):
            vehicle_class=10
        elif (vehicle_class=='sws'):
            vehicle_class=11
        elif (vehicle_class=='Subcompact'):
            vehicle_class=12
        else:
            vehicle_class=13

        engine_size=float(request.form['engine_size'])
        fuel_type=request.form['fuel_type']
        if (fuel_type=='D'):
            fuel_type=0
        elif (fuel_type=='E'):
            fuel_type=1
        elif (fuel_type=='X'):
            fuel_type=2
        else:
            fuel_type=3
        co2_emission=float(request.form['co2_emission'])
        co2_rating=float(request.form['co2_rating'])
        smog_rating=float(request.form['smog_rating'])
        prediction=model.predict(scalar.transform(np.array([[vehicle_class,engine_size,fuel_type,co2_emission,co2_rating,smog_rating]]).reshape(1,-1)))
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Your fuel consumption is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
