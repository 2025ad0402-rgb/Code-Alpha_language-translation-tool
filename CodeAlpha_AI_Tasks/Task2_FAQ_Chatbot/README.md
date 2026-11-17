
# Task 2 – FAQ Chatbot

A Flask-based FAQ chatbot. It stores question-and-answer pairs in `faq_data.json`, converts FAQ questions into TF-IDF vectors, compares a user's question with them using cosine similarity, and returns the closest answer.

## Requirements
- Python 3.9 or newer

## Run on Windows
1. Extract this folder.
2. Open Command Prompt in this folder.
3. Create a virtual environment (recommended):
   `python -m venv venv`
4. Activate it:
   `venv\Scripts\activate`
5. Install packages:
   `pip install -r requirements.txt`
6. Start the chatbot:
   `python app.py`
7. Open `http://127.0.0.1:5000` in your browser.

## Run on macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```
Then open `http://127.0.0.1:5000`.

## How it works
1. FAQs are loaded from `faq_data.json`.
2. `TfidfVectorizer` preprocesses the FAQ questions and converts them into numerical vectors.
3. `cosine_similarity` compares the user's question with all stored questions.
4. The chatbot displays the answer for the highest-scoring match.
5. If the similarity is too low, it asks the user to rephrase the question.

## Add your own FAQs
Open `faq_data.json` and add another object using this format:
```json
{
  "question": "Your question here?",
  "answer": "Your answer here."
}
```
Keep the JSON commas and quotation marks valid. Restart the app after editing the FAQ file.

## Main files
- `app.py` – Flask app and TF-IDF/cosine similarity logic
- `faq_data.json` – editable FAQ question-answer dataset
- `templates/index.html` – chatbot user interface
- `requirements.txt` – Python dependencies
