# Webpage Summarizer

A Python-based tool that:
- Scrapes a webpage for text content.
- Uses OpenAI's GPT models to generate an executive summary that even a 5-year-old can understand.
- Features a GUI for easy user interaction.

---

## Features
- Extracts text content from any webpage using `BeautifulSoup`.
- Summarizes the text with OpenAI's GPT models.
- User-friendly graphical interface (GUI) eliminates the need for manual file management.
- Displays results directly in the GUI.

---

## Requirements
Before running the project, ensure you have the following installed:
- **Python 3.7 or higher**
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `openai`
  - `tkinter` (pre-installed with Python on most platforms)

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Set Up the Environment**:
   - Install the required libraries:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set Up Your OpenAI API Key**:
   - Obtain your OpenAI API key from the [OpenAI Platform](https://platform.openai.com/).
   - Create a `.env` file in the project directory and add your API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

---

## Usage

Run the script from the terminal or command line:
```bash
python Gui.py
```

### How to Use:
1. Launch the GUI.
2. Enter the URL of the webpage you want to summarize.
3. Click the **"Summarize"** button.
4. View the summary directly in the GUI.

---

## Project Structure
- **`Gui.py`**: Main script featuring a graphical user interface for scraping and summarizing.
- **`requirements.txt`**: List of required Python libraries.
- **`README.md`**: Documentation for the project.

---

## Limitations
- Dynamic webpages that load content with JavaScript may not be fully supported. For such cases, consider using Selenium or Playwright.
- Summarization relies on the OpenAI API; ensure your API key has access to the necessary models.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Future Enhancements
- Add support for dynamic webpage scraping using Selenium.
- Provide an option to save both the summary and raw text in different formats (e.g., JSON, Markdown).
- Add export functionality to save summaries directly from the GUI.

---

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests.

---

## Acknowledgments
- [OpenAI](https://openai.com/) for the GPT models.
- Python libraries: `requests`, `beautifulsoup4`, `openai`, and `tkinter`.
