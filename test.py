import requests

# URL of the API
url = 'https://dummyjson.com/products'

# Sending a GET request to the API
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the JSON data
    data = response.json()
    
    # Displaying the first index item
    if 'products' in data and len(data['products']) > 0:
        first_item = data['products'][0]
        print("First index item:", first_item)
    else:
        print("No products found in the JSON response.")
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
