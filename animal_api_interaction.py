import requests
import json

# Replace with your actual API key
API_KEY = "h7xOFO4HJUCo2/vL0+ZpOg==inaDKdO3kHWscZcv"

def get_animal_data(animal_name):
    """
    Fetches data for a specific animal from the Animals API.

    Args:
        animal_name (str): The name of the animal to search for.

    Returns:
        dict or None: A dictionary containing the API response in JSON format,
                     or None if an error occurred.
    """
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None

if __name__ == "__main__":
    animal_to_search = input("Enter the name of an animal you want to search for: ")
    animal_data = get_animal_data(animal_to_search)

    if animal_data:
        print("\nAPI Response:")
        print(json.dumps(animal_data, indent=4))
    else:
        print(f"\nCould not retrieve data for '{animal_to_search}'.")

    # Test with a non-existent animal
    non_existent_animal = "thisanimaldoesnotexist"
    non_existent_data = get_animal_data(non_existent_animal)

    if non_existent_data is not None:
        print(f"\nResponse for non-existent animal '{non_existent_animal}':")
        print(json.dumps(non_existent_data, indent=4))
    else:
        print(f"\nCould not retrieve data for '{non_existent_animal}'.")