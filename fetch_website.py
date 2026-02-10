import requests
from bs4 import BeautifulSoup

def fetch_and_summarize(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        paragraphs = soup.find_all('p')
        summary = f"Title: {title}\n\nSummary:\n"
        for p in paragraphs:
            summary += p.get_text() + '\n\n'
        return summary
    except requests.RequestException as e:
        return f"Error fetching the URL: {e}"

def main():
    url = "https://www.usc.edu/"
    summary = fetch_and_summarize(url)
    print(summary)

if __name__ == "__main__":
    main()