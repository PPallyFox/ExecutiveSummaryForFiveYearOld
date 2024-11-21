import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
import openai

# Replace with your OpenAI API key
openai.api_key = "API-KEY"

# Function to scrape the webpage
def scrape_webpage(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator='\n')
        return text.strip()
    except Exception as e:
        return f"Error scraping webpage: {e}"

# Function to summarize text using OpenAI
def get_summary(text):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Summarize this for a 5-year-old: {text}"}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating summary: {e}"

# Function to handle the scraping and summarizing process
def process_url():
    url = url_entry.get()
    if not url:
        result_label.config(text="Please enter a valid URL.")
        return

    # Scrape the webpage
    scraped_text = scrape_webpage(url)
    if "Error" in scraped_text:
        result_label.config(text=scraped_text)
        return

    # Generate the summary
    summary = get_summary(scraped_text)
    if "Error" in summary:
        result_label.config(text=summary)
        return

    # Display the summary
    result_label.config(text=f"Summary:\n{summary}")

# GUI setup
root = tk.Tk()
root.title("Webpage Summarizer")

# Input field
url_label = ttk.Label(root, text="Enter URL:")
url_label.pack(pady=5)
url_entry = ttk.Entry(root, width=50)
url_entry.pack(pady=5)

# Submit button
submit_button = ttk.Button(root, text="Summarize", command=process_url)
submit_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", wraplength=400, justify="left")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
