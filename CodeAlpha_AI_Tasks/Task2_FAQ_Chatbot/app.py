
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from pathlib import Path

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("faq_data.json")

with DATA_FILE.open(encoding="utf-8") as f:
    FAQS = json.load(f)

# Build the TF-IDF index once when the app starts.
faq_questions = [item["question"] for item in FAQS]
vectorizer = TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2))
faq_matrix = vectorizer.fit_transform(faq_questions)

def find_best_answer(user_question):
    query_vector = vectorizer.transform([user_question])
    scores = cosine_similarity(query_vector, faq_matrix).flatten()
    best_index = int(scores.argmax())
    best_score = float(scores[best_index])
    if best_score < 0.12:
        return {
            "answer": "Sorry, I could not find a close FAQ match. Please rephrase your question or add it to faq_data.json.",
            "matched_question": None,
            "similarity": round(best_score * 100, 1),
            "matched": False
        }
    return {
        "answer": FAQS[best_index]["answer"],
        "matched_question": FAQS[best_index]["question"],
        "similarity": round(best_score * 100, 1),
        "matched": True
    }

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/ask")
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify(error="Please type a question."), 400
    if len(question) > 500:
        return jsonify(error="Please keep your question under 500 characters."), 400
    return jsonify(find_best_answer(question))

@app.get("/faqs")
def faqs():
    return jsonify(FAQS)

if __name__ == "__main__":
    app.run(debug=True)
