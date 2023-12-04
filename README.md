# CRS-Conversion
This is a simple API which will convert XY Coordinate Reference System(CRS) values to Lat/Lng

**Requirements**
1. Python 3 


**How to run**
1. Checkout the code
2. Install Flask (pip install Flask)
3. Install "pyproj" (pip install pyproj)
4. Run the project (python app.py)
5. Then the API will be running on port 5000


**Sample Request/Response**
![image](https://github.com/eranthaWELIKALA/CRS-Conversion/assets/33684206/a70ca81e-3482-464a-8e9c-1e81027791f7)


**cURL Command**
curl  -X POST \
  'http://127.0.0.1:5000/convert' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "crs": 2278,
  "x": 3111223.07202555,
  "y": 13856839.923629
}'
