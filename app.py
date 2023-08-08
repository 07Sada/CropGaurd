from config import crop_model, crop_pipeline_encoder, crop_label_encoder
from config import fertilizer_model, fertilizer_pipeline_encoder, fertilizer_label_encoder
from config import plant_diseases_classifier_model
from utils import retrieve_image_by_name_from_mongodb, retrieve_data
from flask import Flask, request, render_template, jsonify
import requests
import os
import numpy as np
import base64

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploaded_image'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/crop_recommendation', methods=['GET', 'POST'])
def crop_recommendation():
    return render_template('crop_recommendation_input.html')

@app.route("/crop_recommendation_output", methods=['GET', 'POST'])
def crop_recommendation_output():
    temperature = request.form.get("temperature")
    humidity = request.form.get("humidity")
    ph = request.form.get("ph")
    nitrogen = request.form.get("nitrogen")
    potassium = request.form.get("potassium")
    phosphorous = request.form.get("phosphorous")
    rain_fall = request.form.get("rain_fall")

    input_list = [nitrogen, phosphorous, potassium, temperature, humidity, ph, rain_fall]
    input_array = np.array(input_list).reshape(-1, 7).astype(int)

    transformed_data = crop_pipeline_encoder.transform(input_array)
    model_prediction = crop_model.predict(transformed_data).astype(int)

    label = crop_label_encoder.inverse_transform(model_prediction)
    
    # retrieving the image from mongodb dabase
    image_data = retrieve_image_by_name_from_mongodb(database_name=os.getenv("CROP_DB_NAME"),
                                                        collection_name=os.getenv("CROP_IMAGE_COLLECTION_NAME"),
                                                        file_name=str(label[0]))

    # encoding the byte data recieved from the mongodb
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')

    # retrieving text data from mongodb 
    crop_details = retrieve_data(database_name=os.getenv("CROP_DB_NAME"), collection_name= os.getenv("CROP_INFO_COLLECTION_NAME"), search_query=label[0])

    return render_template('crop_recommendation_output.html', image_data_base64=image_data_base64, input_file_name=label[0], crop_details=crop_details)


@app.route('/fertilizer_recommendation', methods=['GET', 'POST'])
def fertilizer_recommendation():
    return render_template('fertilizer_recommendation_input.html')

@app.route('/fertilizer_recommendation_output', methods=['GET', 'POST'])
def fertilizer_recommendation_output():
    temperature = request.form.get("temperature")
    humidity = request.form.get("humidity")
    moisture = request.form.get("moisture")
    nitrogen = request.form.get("nitrogen")
    potassium = request.form.get("potassium")
    phosphorous = request.form.get("phosphorous")
    soil_type = request.form.get("soil_type")
    crop_type = request.form.get("crop_type")

    input_data = [int(temperature), int(humidity), int(moisture), soil_type, crop_type, int(nitrogen), int(potassium), int(phosphorous)]
    input_array = np.array(input_data).reshape(-1, 8)
    
    transformed_data = fertilizer_pipeline_encoder.transform(input_array)
    model_prediction = fertilizer_model.predict(transformed_data).astype(int)

    label = fertilizer_label_encoder.inverse_transform(model_prediction)

    # retrieving the image from mongodb dabase
    image_data = retrieve_image_by_name_from_mongodb(database_name=os.getenv("FERTILIZER_DB_NAME"),
                                                        collection_name=os.getenv("FERTILIZER_IMAGE_COLLECTION_NAME"),
                                                        file_name=str(label[0]))
    
    # encoding the byte data recieved from the mongodb
    image_data_base64 = base64.b64encode(image_data).decode('utf-8')

    # retrieving text data from mongodb 
    fertilizer_details = retrieve_data(database_name=os.getenv("FERTILIZER_DB_NAME"), collection_name= os.getenv("FERTILIZER_INFO_COLLECTION_NAME"), search_query=label[0])


    return render_template('fertilizer_recommendation_ouput.html', image_data_base64=image_data_base64, label= label[0], fertilizer_details=fertilizer_details)


@app.route('/image_classification', methods=['GET', 'POST'])
def image_classification():
    return render_template('image_classification_input.html')

@app.route('/image_classification_output', methods=['GET', 'POST'])
def image_classification_output():
    file = request.files['image_file']
    new_filename = "plant_image.JPG"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)

    # infercing the with the uploaded image
    results = plant_diseases_classifier_model(file_path)
    
    #fetching all the labels 
    names_dict = results[0].names

    # fetching the probalility of each class
    probs = results[0].probs.data.tolist()

    # selecting class with maximum probability
    model_prediction= names_dict[np.argmax(probs)]

    diseases_details = retrieve_data(database_name=os.getenv("DISEASE_DB_NAME"), 
                                    collection_name=os.getenv("DISEASE_INFO_COLLECTION_NAME"),
                                    search_query=model_prediction)

    return render_template("image_classification_output.html", model_prediction=model_prediction, diseases_details=diseases_details)


@app.route('/market_price')
def market_price():
    return render_template("market_price_input.html")

@app.route('/market_price_output', methods=['POST'])
def market_price_output():
    # input field name is 'selected_state'
    user_input = request.form.get('selected_state')
    api_key = os.getenv("COMMODITY_PRICE_API_KEY")

    # Make a request to the API with the user input
    api_url = f'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={api_key}&format=json&filters%5Bstate%5D={user_input}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        data = data['records']
        # return render_template('market_price_output.html', data=data)
        if len(data) > 0:
        # Return the JSON data as a response
            return render_template('market_price_output.html', data=data)
        else:
            return render_template("market_price_no_data.html")
    else:
        return jsonify({'error': 'Unable to fetch data from the API'}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)