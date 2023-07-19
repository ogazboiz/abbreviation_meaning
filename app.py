from flask import Flask, jsonify, request, make_response, render_template
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


with open('abbreviations.json') as file:
    abbreviations = json.load(file)

@app.route('/')
def index():
    return render_template('index.html')
# API endpoint to handle abbreviation requests
@app.route('/api/abbreviation/<abbr>')
def get_abbreviation(abbr):
    abbreviation = abbr.upper()
    full_name = abbreviations.get(abbreviation) or abbreviations.get(abbreviation.lower())

    if full_name:
        response = jsonify({'abbreviation': abbreviation, 'Meaning': full_name})
        return response
    else:
        return make_response(jsonify({'error': 'This abbreviation does not exist in our records.'}), 404)
# @app.route('/api/abbreviation/<abbr>')
# def get_abbreviation(abbr):
#     abbreviation = abbr.upper()
#     full_name = abbreviations.get(abbreviation) or abbreviations.get(abbreviation.lower())

#     if full_name:
#         response = jsonify({'abbreviation': abbreviation, 'Meaning': full_name})
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     else:
#         return make_response(jsonify({'error': 'This entry does not exist in our records as of yet :( \n\n1. You can help us add this by creating a GitHub issue\n\n2. Or, you could fill out this feedback form and we will address the issue'}), 404)

# Start the server
if __name__ == '__main__':
    app.run( debug=True, port=5000)
