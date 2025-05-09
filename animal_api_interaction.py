import requests
import json

# Replace with your actual API key
API_KEY = "h7xOFO4HJUCo2/vL0+ZpOg==inaDKdO3kHWscZcv"

def fetch_animal_data(animal_name):
    """Fetches animal data from the API."""
    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def generate_website(animals):
    """Generates the HTML website from the animal data."""
    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Animals</title>
</head>
<body>
    <h1>Animals</h1>
"""
    if animals:
        for animal in animals:
            html_content += f"<div><h2>{animal.get('name', 'Unknown')}</h2>"
            # Add more details you want to display from the API response
            if 'taxonomy' in animal:
                html_content += f"<p>Kingdom: {animal['taxonomy'].get('kingdom', 'N/A')}</p>"
                html_content += f"<p>Phylum: {animal['taxonomy'].get('phylum', 'N/A')}</p>"
                # Add other taxonomic information as needed
            if 'characteristics' in animal:
                html_content += f"<p>Lifespan: {animal['characteristics'].get('lifespan', 'N/A')}</p>"
                html_content += f"<p>Habitat: {animal['characteristics'].get('habitat', 'N/A')}</p>"
                # Add other characteristics as needed
            html_content += "</div><hr>"
    else:
        html_content += "<p>No animals found.</p>"

    html_content += """
</body>
</html>
"""
    with open("animals.html", "w") as f:
        f.write(html_content)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    animal_name_to_search = "Fox"
    fox_data = fetch_animal_data(animal_name_to_search)
    if fox_data:
        generate_website(fox_data)
    else:
        generate_website([]) # Generate an empty website or handle the error as you see fitnot retrieve data for '{non_existent_animal}'.")\nCould not retrieve data for '{non_existent_animal}'.")