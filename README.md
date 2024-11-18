# README

## Project: Extract Versioned Lecture URLs

This Python script extracts lecture-specific URLs from the schedule page of Stanford's CS106B course and formats them to match a versioned base URL structure. The processed URLs are saved to a text file for further use.

### Features
- Scrapes URLs from the CS106B schedule page.
- Filters lecture-specific URLs.
- Formats URLs to match a versioned base URL structure.
- Saves the processed URLs to a text file.

### Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

### Setup
1. Clone or download the repository.
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4
   ```

### Usage
1. Update the `url` and `versioned_base_url` variables in the script as needed.
2. Run the script:
   ```bash
   python extract_versioned_urls.py
   ```
3. The extracted URLs will be saved in `versioned_lecture_urls.txt`.

### Output
- `versioned_lecture_urls.txt`: A file containing the formatted lecture URLs, one per line.

### Notes
- Ensure the schedule URL is accessible and matches the expected structure for proper functionality.
- Modify the URL patterns in the script if the course structure changes. Use them for any archive version.

Enjoy extracting and organizing lecture URLs efficiently!
