import requests

def fetch_data_from_api(url):
    try:
        # Perform the API call
        response = requests.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Parse the JSON response
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None

# Example usage:
if __name__ == "__main__":
    university_data_url = "http://universities.hipolabs.com/search"
    country_info_data_url = "https://restcountries.com/v3.1/all"
    
    print("Fetching university data...")
    university_data = fetch_data_from_api(university_data_url)
    if university_data:
        print(f"Retrieved {len(university_data)} universities.")
    
    print("Fetching country info data...")
    country_info_data = fetch_data_from_api(country_info_data_url)
    if country_info_data:
        print(f"Retrieved {len(country_info_data)} countries.")