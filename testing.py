import requests
from bs4 import BeautifulSoup

# Original schedule URL
url = 'https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1246/schedule.html'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

# Define the versioned base URL
versioned_base_url = 'https://web.stanford.edu/class/archive/cs/cs106b/cs106b.1246/lectures/'

# List to store only the lecture-specific URLs in versioned format
versioned_lecture_urls = []

# Extract and filter URLs
for link in soup.find_all('a', href=True):
    href = link['href']
    
    # Check if the link follows the non-versioned base URL format
    if href.startswith('/class/cs106b/lectures/') or href.startswith('https://web.stanford.edu/class/cs106b/lectures/'):
        
        # Extract just the lecture folder name (e.g., '01-welcome/')
        lecture_folder = href.split('/')[-2] + '/'  # Get the folder from the URL
        
        # Construct the versioned URL and add to the list
        versioned_lecture_urls.append(versioned_base_url + lecture_folder)

# Save the versioned URLs to a text file
with open("versioned_lecture_urls.txt", "w") as file:
    for versioned_url in versioned_lecture_urls:
        file.write(versioned_url + "\n")

print("Versioned lecture URLs have been saved to versioned_lecture_urls.txt.")