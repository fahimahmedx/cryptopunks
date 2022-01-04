from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        # Type
        Type = request.form['Type']
        if Type == "Alien":
            Type = 4
        elif Type == "Ape":
            Type = 3
        elif Type == "Zombie":
            Type = 2
        elif Type == "Female":
            Type = 1
        elif Type == "Male":
            Type = 0
        else:
            return render_template('index.html',prediction_texts="Type entered incorrectly.")
        
        # Attribute Count
        AttributeCount = int(request.form['AttributeCount'])

        # Attributes
        allAttributes = ['Beanie',
                        'Choker',
                        'Pilot Helmet',
                        'Tiara',
                        'Orange Side',
                        'Buck Teeth',
                        'Welding Goggles',
                        'Pigtails',
                        'Pink With Hat',
                        'Top Hat',
                        'Spots',
                        'Rosy Cheeks',
                        'Blonde Short',
                        'Wild White Hair',
                        'Cowboy Hat',
                        'Wild Blonde',
                        'Straight Hair Blonde',
                        'Big Beard',
                        'Red Mohawk',
                        'Half Shaved',
                        'Blonde Bob',
                        'Vampire Hair',
                        'Clown Hair Green',
                        'Straight Hair Dark',
                        'Straight Hair',
                        'Silver Chain',
                        'Dark Hair',
                        'Purple Hair',
                        'Gold Chain',
                        'Medical Mask',
                        'Tassle Hat',
                        'Fedora',
                        'Police Cap',
                        'Clown Nose',
                        'Smile',
                        'Cap Forward',
                        'Hoodie',
                        'Front Beard Dark',
                        'Frown',
                        'Purple Eye Shadow',
                        'Handlebars',
                        'Blue Eye Shadow',
                        'Green Eye Shadow',
                        'Vape',
                        'Front Beard',
                        'Chinstrap',
                        '3D Glasses',
                        'Luxurious Beard',
                        'Mustache',
                        'Normal Beard Black',
                        'Normal Beard',
                        'Eye Mask',
                        'Goat',
                        'Do-rag',
                        'Shaved Head',
                        'Muttonchops',
                        'Peak Spike',
                        'Pipe',
                        'VR',
                        'Cap',
                        'Small Shades',
                        'Clown Eyes Green',
                        'Clown Eyes Blue',
                        'Headband',
                        'Crazy Hair',
                        'Knitted Cap',
                        'Mohawk Dark',
                        'Mohawk',
                        'Mohawk Thin',
                        'Frumpy Hair',
                        'Wild Hair',
                        'Messy Hair',
                        'Eye Patch',
                        'Stringy Hair',
                        'Bandana',
                        'Classic Shades',
                        'Shadow Beard',
                        'Regular Shades',
                        'Horned Rim Glasses',
                        'Big Shades',
                        'Nerd Glasses',
                        'Black Lipstick',
                        'Mole',
                        'Purple Lipstick',
                        'Hot Lipstick',
                        'Cigarette',
                        'Earring']
        Attributes = [0] * len(allAttributes)
        # change index to 1 if certain attribute exists
        for i in range(len(allAttributes)):
            if allAttributes[i].lower() in request.form['Attributes'].lower():
                Attributes[i] = 1

        prediction=model.predict([[Type, AttributeCount] + Attributes])
        output=round(prediction[0],2)
        return render_template('index.html',prediction_text="This NFT has a predicted value of {} ETH".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

