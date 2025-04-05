
import requests
def get_alai_access_token(email, password):
    auth_url = "https://api.getalai.com/auth/v1/token?grant_type=password"
    headers = {
        "Content-Type": "application/json",
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVzY2hvdHRoamdsamJ4amVyY3puIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTAxMTI0NzYsImV4cCI6MjAyNTY4ODQ3Nn0.3pZ7fQ9qWjBcX-oSLJ37P4D9ojrdTF1zdI1B4ONcxrE"
    }
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(auth_url, json=payload, headers=headers)
    print("Status:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data["access_token"]
    else:
        print("Error", response.status_code, response.text)
        return None

def update_alai_presentation(access_token, presentation_id, slides):
    url = "https://alai-standalone-backend.getalai.com/get-calibration-sample-text"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "presentation_id": presentation_id,
        "raw_context": str(slides)
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("✅ Presentation Updated:")
        return f"https://app.getalai.com/presentation/{presentation_id}"
    else:
        print("❌ Update Failed:", response.status_code, response.text)
        return None
