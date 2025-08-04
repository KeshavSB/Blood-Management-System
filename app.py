from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gksb@5568",  # Change to your MySQL password
        database="bloodmanagementsystem"
    )

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Blood Management System API!"})


# ✅ Route to add a new donor
@app.route('/donors', methods=['POST'])
def add_donor():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Donors (name, age, contact, blood_type, donation_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (data['name'], data['age'], data['contact'], data['blood_type'], data['donation_date']))
        conn.commit()
        return jsonify({"message": "Donor added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to get all donors
@app.route('/donors', methods=['GET'])
def get_donors():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Donors")
    donors = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(donors)

# ✅ Route to add a new blood bank
@app.route('/bloodbanks', methods=['POST'])
def add_blood_bank():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO BloodBanks (name, location, contact) VALUES (%s, %s, %s)"
        cursor.execute(query, (data['name'], data['location'], data['contact']))
        conn.commit()
        return jsonify({"message": "Blood bank added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to get all blood banks
@app.route('/bloodbanks', methods=['GET'])
def get_blood_banks():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM BloodBanks")
    banks = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(banks)

# ✅ Route to add a recipient
@app.route('/recipients', methods=['POST'])
def add_recipient():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Recipients (name, age, contact, blood_type, request_date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (data['name'], data['age'], data['contact'], data['blood_type'], data['request_date']))
        conn.commit()
        return jsonify({"message": "Recipient added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to update recipient status
@app.route('/recipients/<int:recipient_id>', methods=['PUT'])
def update_recipient_status(recipient_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE Recipients SET status = %s WHERE recipient_id = %s"
        cursor.execute(query, (data['status'], recipient_id))
        conn.commit()
        return jsonify({"message": "Recipient status updated!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to get all recipients
@app.route('/recipients', methods=['GET'])
def get_recipients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Recipients")
    recipients = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(recipients)

# ✅ Route to check blood inventory
@app.route('/bloodinventory', methods=['GET'])
def get_blood_inventory():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM BloodInventory WHERE quantity > 0")
    inventory = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(inventory)

# ✅ Route to update blood inventory
@app.route('/bloodinventory/<int:bank_id>', methods=['PUT'])
def update_blood_inventory(bank_id):
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE BloodInventory SET quantity = %s WHERE inventory_id = %s"
        cursor.execute(query, (data['quantity'], bank_id))
        conn.commit()
        return jsonify({"message": "Blood inventory updated!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to add a bloodinventory
@app.route('/bloodinventory', methods=['POST'])
def add_blood_inventory():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO BloodInventory (bank_id, quantity, expiry_date, blood_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['bank_id'], data['quantity'], data['expiry_date'], data['blood_type']))
        conn.commit()
        return jsonify({"message": "Inventory added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to add a hospital
@app.route('/hospitals', methods=['POST'])
def add_hospital():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO Hospitals (name, location, staff, contact) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data['name'], data['location'], data['staff'], data['contact']))
        conn.commit()
        return jsonify({"message": "Hospital added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# ✅ Route to get all hospitals
@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Hospitals")
    hospitals = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(hospitals)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
