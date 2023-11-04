from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import json

# загружаем модель из файла
with open('https://drive.google.com/file/d/1c0OTzY-64cvr8_d0V4hWtr5IbN2gnKK4/view?usp=drive_link', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

# создаём приложение
app = Flask(__name__)

@app.route('/')
def index():
    msg = "Тестовое сообщение. Сервер запущен!"
    return msg


@app.route('/predict', methods=['POST'])
def predict_func():
	features = request.json
	cols = [    'baths', 'fireplace', 'city', 'sqft', 'zipcode', 'state', 'pool', 'school_max_rating', 'shcool_mean_distance', 
    'Year built', 'Remodeled', 'Heating', 'Cooling', 'Parking', 'propertyType_apartment', 'propertyType_condo',
    'propertyType_family_home', 'propertyType_historical', 'propertyType_land', 'propertyType_mobile_home',
    'propertyType_modern', 'propertyType_other', 'propertyType_ranch', 'propertyType_townhouse']
	features_f = pd.DataFrame([features], columns=cols)
	features_f['zipcode'] = features_f['zipcode'].astype(str)
	features_f['Year built'] = features_f['Year built'].astype(str)
	ler_scaler = preprocessing.RobustScaler()
	for column in ['baths', 'sqft', 'school_max_rating', 'shcool_mean_distance']:
    	features_f[column] = r_scaler.fit_transform(features_f[[column]])[:,0]
	le = LabelEncoder()
 	for column in ['state', 'city', 'zipcode', 'Year built']
		features_f[column] = le.fit_transform(features_f[[column]])[:,0]
	predict = model.predict(features_f)
	return jsonify({'prediction': round(np.exp(predict[0]))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
