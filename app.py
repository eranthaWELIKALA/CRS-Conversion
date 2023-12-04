from flask import Flask, request, jsonify
from pyproj import Transformer

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_coordinates():
    try:
        # Get x, y, and crs from the JSON request
        data = request.get_json()
        x = data['x']
        y = data['y']
        crs = data['crs']

        # Define the transformer with the provided CRS information
        # Texas South Central 2278
        transformer = Transformer.from_crs(crs, 4326, always_xy=True)

        # Transform coordinates
        converted = transformer.transform(x, y)

        # Create a response JSON
        response = {
            'latitude': converted[1],
            'longitude': converted[0]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
