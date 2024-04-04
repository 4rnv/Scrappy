import requests
from bs4 import BeautifulSoup
import time
         
wayback_url = "http://web.archive.org/save"     
webpage_url = input("Enter the full URL of the webpage you want to scrape (include https://): ")
response = requests.get(webpage_url)
soup = BeautifulSoup(response.content, "html.parser")
         
a_links = soup.find_all("a")
print(a_links)
         
urls_to_save = []
         
for tag in a_links:
    print(f"Do you want to save URL {tag}? Press 1 for yes, 0 for no.")
    user_cha_response = int(input())
    if user_cha_response==1:
        href = tag.get("href")
        if href and href.startswith("http"):
                urls_to_save.append(href)

successful_urls = []
failed_urls = []
for url in urls_to_save:
    payload = {"url": url}
    response = requests.post(wayback_url, data=payload)
    if response.status_code == 200:
        print(f"URL {url} saved to the Wayback Machine!")
        successful_urls.append(url)
        time.sleep(5)
    else:
        print(f"Failed to save URL {url} to the Wayback Machine.")
        failed_urls.append(url)
        time.sleep(5)
        
print("Successful URLs: ", successful_urls)
print("Failed URLs: ", failed_urls)

# Single retry for failed URLS, you could add another loop for multiple retries, but it will probably get blocked
if len(failed_urls) != 0:
        print("Do you want to retry for failed URLs?Enter 1 for yes, 0 for no.")
        user_retry = int(input())
        if user_retry == 1:
                for url in failed_urls:
                        payload = {"url": url}
                        response = requests.post(wayback_url, data=payload)
                        if response.status_code == 200:
                                print(f"URL {url} saved to the Wayback Machine on retry attempt!")
                        else:
                                print(f"Unable to save URL {url} to the Wayback Machine after retry attempt!")