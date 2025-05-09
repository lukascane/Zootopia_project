import data_fetcher
import json

def generate_website(animals, searched_animal=""):
    """Generates the HTML website from the animal data."""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Animals</title>
</head>
<body>
    <h1>Animals</h1>
    <h2>Results for "{searched_animal}"</h2>
"""
    if animals:
        for animal in animals:
            html_content += f"<div><h2>{animal.get('name', 'Unknown')}</h2>"
            if 'taxonomy' in animal:
                html_content += f"<p>Kingdom: {animal['taxonomy'].get('kingdom', 'N/A')}</p>"
                html_content += f"<p>Phylum: {animal['taxonomy'].get('phylum', 'N/A')}</p>"
            if 'characteristics' in animal:
                html_content += f"<p>Lifespan: {animal['characteristics'].get('lifespan', 'N/A')}</p>"
                html_content += f"<p>Habitat: {animal['characteristics'].get('habitat', 'N/A')}</p>"
            html_content += "</div><hr>"
    else:
        html_content += f"<h2>The animal \"{searched_animal}\" doesn't exist.</h2>"

    html_content += """
</body>
</html>
"""
    with open("animals.html", "w") as f:
        f.write(html_content)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")
    animal_data = data_fetcher.fetch_data(animal_name)
    generate_website(animal_data, animal_name)