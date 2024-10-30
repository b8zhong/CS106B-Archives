import requests
from bs4 import BeautifulSoup

url = 'https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1246/schedule.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

base_url = 'https://web.stanford.edu/class/cs106b/lectures/'
full_base_url = 'https://web.stanford.edu'

# List to store only the lecture-specific URLs
lecture_urls = []

# Extract and filter URLs
for link in soup.find_all('a', href=True):
    href = link['href']
    
    # Adjust for relative links starting with '/'
    if href.startswith('/class/cs106b/lectures/'):
        href = full_base_url + href  # Construct the full URL
    
    # Check if the href contains the base URL structure
    if href.startswith(base_url):
        lecture_urls.append(href)

# Output the filtered URLs
for lecture_url in lecture_urls:
    print(lecture_url)