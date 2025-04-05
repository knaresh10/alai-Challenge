
from dotenv import load_dotenv
import os
load_dotenv()
from scraper import scrape_webpage
from alai_api import get_alai_access_token, update_alai_presentation

def generate_presentation_from_webpage(url, email, password, presentation_id):
    content = scrape_webpage(url)
    if not content:
        print("No content extracted.")
        return None

    access_token = get_alai_access_token(email, password)
    if not access_token:
        print("Authentication failed.")
        return None

    print("Generating slides...")
    slides = [{"content": section.strip()} for section in content['markdown'].split("\n") if section.strip()][:5]

    print("Updating Alai Presentation...")
    presentation_link = update_alai_presentation(access_token, presentation_id, slides)

    if presentation_link:
        print("✅ Alai Presentation Updated:", presentation_link)
    else:
        print("❌ Failed to update presentation.")

# Run script
if __name__ == "__main__":
    website_url = "https://workat.tech/programs/flipkart-gwc-6/dashboard"  # ✅ Put your target URL here
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    presentation_id = "b89be55a-3cd6-47b0-a389-8a7c2ef6d0e6"  # ✅ Use your actual presentation ID

    generate_presentation_from_webpage(website_url, email, password, presentation_id)