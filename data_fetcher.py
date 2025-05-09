from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY environment variable not set. Please create a .env file.")
    exit()

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
    # Example usage if you want to run data_fetcher.py directly
    animal_to_search = input("Enter an animal name to fetch data: ")
    data = fetch_data(animal_to_search)
    if data:
        print(json.dumps(data, indent=4))
    else:
        print(f"No data fetched for '{animal_to_search}'.")