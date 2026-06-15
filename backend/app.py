from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 75000
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 30000
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 5000
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 12000
    }
]

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route('/products')
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5002,
        debug=True
    )
