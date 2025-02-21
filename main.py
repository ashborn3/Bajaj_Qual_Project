from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Hardcoded user details
USER_ID = "Nitin_Chauhan_22BAI71270"
EMAIL = "22BAI71270@cuchd.in"
ROLL_NUMBER = "22BAI71270"

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.get_json()
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        numbers = []
        alphabets = []
        for item in data['data']:
            item_str = str(item)
            if item_str.isdigit():
                numbers.append(item_str)
            elif item_str.isalpha():
                alphabets.append(item_str)
            else:
                return jsonify({"is_success": False, "message": "Invalid data format"}), 400
        
        highest_alphabet = [max(alphabets, key=lambda x: x.lower())] if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)