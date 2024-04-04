A Python script to scrape URLs from a webpage and archive them to the Wayback machine. Uses Beautiful Soup to parse a page for anchor tags and then saves them using the Archive.org API. The name is supposed to be scrap.py as in scrapping plus python.

# Usage

Clone or ZIP this repo. Install the modules mentioned in `requirements.txt` using `pip install -r requirements.txt`. Then run the script in your terminal and follow the screen instructions.


IMPORTANT: `time.sleep(5)` delays archival of each URL for 5 seconds. This is to avoid overloading the API with excess requests, due to which sometimes the server refuses the connection. A healthy gap between each request prevents that.
