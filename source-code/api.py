from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import joblib

app = Flask(__name__)
CORS(app, origins="*")

model = joblib.load("linear_regression_model.joblib")

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    print(request.get_json())
    try:
        data = request.get_json(force=True)
        team_exp = float(data['TeamExp'])
        manager_exp = float(data['ManagerExp'])
        year_end = int(data['YearEnd'])
        length = int(data['Length'])

        # Input validation checks
        if team_exp < 0 or manager_exp < 0 or year_end < 0 or length < 0:
            raise ValueError('All input values must be positive')
            
        prediction = model.predict([[team_exp, manager_exp, year_end, length]])
        return jsonify({'prediction': list(prediction)})
    except (ValueError, KeyError, TypeError):
        # Error handling - returns a 400 Bad Request response
        return jsonify({'error': 'Invalid input data'}, 400)

if __name__ == '__main__':
    app.run(port=5000, debug=True)