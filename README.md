# News Sentiment CLI Tool
[![CS50P Certified](https://img.shields.io/badge/CS50P-Certified-brightgreen?style=for-the-badge&logo=python&logoColor=white)](https://cs50.harvard.edu/certificates/db9372a3-2954-4849-bb04-92b305aa2038)

#### Video Demo: https://youtu.be/6DG1rt_VY7c
#### Certificate: https://cs50.harvard.edu/certificates/db9372a3-2954-4849-bb04-92b305aa2038

---

#### Description:
The News Sentiment CLI Tool is a command-line application written in Python that allows users to fetch recent news headlines on any topic and analyze their sentiment using natural language processing.

This tool was developed as my final project for Harvard's CS50's Introduction to Programming with Python. The goal was to build a practical tool that demonstrates API integration, text processing, command-line interaction, and testing — all wrapped into a clean, testable Python project.

When the user enters a topic (e.g., "gold", "AI", "elections"), the tool fetches up to 10 recent news headlines related to that topic using the NewsAPI. It then performs sentiment analysis on each headline using the TextBlob library and prints each headline with a sentiment score ranging from -1 (negative) to +1 (positive). Finally, it calculates and prints the average sentiment across all headlines.

---

### Files and Their Purpose:

- **project.py**
  This is the main file that contains:
  - `main()`: handles user input and coordinates function calls
  - `fetch_headlines()`: uses NewsAPI to fetch news headlines
  - `analyze_sentiments()`: analyzes each headline’s sentiment
  - `print_summary()`: displays sentiment scores and an average

- **test_project.py**
  Contains test functions written with `pytest` to validate:
  - That `fetch_headlines()` returns a list of strings
  - That `analyze_sentiments()` returns float sentiment scores
  - That the tool handles edge cases like empty input gracefully

- **requirements.txt**
  Lists the libraries needed: `requests`, `textblob`, `python-dotenv`

- **.env**
  Stores the API key securely (not pushed to GitHub)

- **.gitignore**
  Prevents sensitive or unnecessary files like `.env` and `__pycache__` from being tracked in Git

- **README.md**
  This file describes the purpose and structure of the project.

---

### How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Add your NewsAPI key to a `.env` file:
    ```
    NEWS_API_KEY=your_api_key_here
    ```

3. Run the program:
    ```
    python project.py
    ```

---

### Design Choices

- I used the `requests` library to make API calls, as it's lightweight and beginner-friendly.
- The project uses `TextBlob` for sentiment analysis due to its simplicity and good-enough performance for short headlines.
- I chose to write all the required functions in `project.py` to stay within CS50’s guidelines, even though I would normally separate code into modules.
- The decision to print results in the CLI instead of building a web interface kept the focus on core Python.

---

### Testing

I used `pytest` to test all core logic:
- Data returned from the API is the correct type
- Sentiment analysis returns expected results
- Edge cases (like empty input) are handled

---

### Future Improvements

- Add support for exporting results to CSV
- Let users choose number of headlines or output format
- Replace TextBlob with a more advanced model like VADER or spaCy
- Build a web dashboard with Flask or Streamlit

---

This project reflects what I’ve learned through CS50 and my growth as a beginner in data science and Python development.
