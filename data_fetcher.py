import requests
import json

API_KEY = "h7xOFO4HJUCo2/vL0+ZpOg==inaDKdO3kHWscZcv"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name' from the API.
    Returns: a list of animals, each animal is a dictionary in the specified format.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for '{animal_name}': {e}")
        return None

if __name__ == "__main__":

    animal_to_search = input("Enter an animal name to fetch data: ")
    data = fetch_data(animal_to_search)
    if data:
        print(json.dumps(data, indent=4))
    else:
        print(f"No data fetched for '{animal_to_search}'.")