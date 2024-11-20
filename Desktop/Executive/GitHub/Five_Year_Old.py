from bs4 import BeautifulSoup
import requests
import openai
import sys

# Step 1: Scrape Webpage
def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator='\n')  # Extract readable text
    return text.strip()

# Step 2: Save Text to File
def save_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Text saved to {filename}")

# Step 3: Get Summary from ChatGPT
def get_summary(text):
    openai.api_key = "API-KEY"  # Replace with your OpenAI API key
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize this for a 5-year-old: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Main Program
if __name__ == "__main__":
    # Check for correct number of parameters
    if len(sys.argv) < 3:
        print("Usage: python script.py <URL> <output_filename>")
        sys.exit(1)

    # Get parameters from command line
    url = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        # Step 1: Scrape Webpage
        print("Scraping webpage...")
        web_text = scrape_webpage(url)
        
        # Step 2: Save to File
        print("Saving text to file...")
        save_to_file(web_text, output_filename)

        # Step 3: Generate Summary
        print("Generating summary...")
        summary = get_summary(web_text)
        print("\nExecutive Summary:")
        print(summary)
    except Exception as e:
        print(f"An error occurred: {e}")
