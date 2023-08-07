from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route('/crop_recommendation')
def crop_recommendation():
    return render_template('crop_recommendation_input.html')

@app.route('/fertilizer_recommendation')
def fertilizer_recommendation():
    return render_template('fertilizer_recommendation_input.html')

@app.route('/image_classification')
def image_classification():
    return render_template('image_classification_input.html')

@app.route('/market_price')
def market_price():
    return render_template("market_price_input.html")

@app.route('/market_price_output', methods=['POST'])
def market_price_output():
    # input field name is 'selected_state'
    user_input = request.form.get('selected_state')
    api_key = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"

    # Make a request to the API with the user input
    api_url = f'https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key={api_key}&format=json&filters%5Bstate%5D={user_input}'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        data = data['records']
        # Return the JSON data as a response
        return render_template('market_price_output.html', data=data)
    else:
        return jsonify({'error': 'Unable to fetch data from the API'}), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)