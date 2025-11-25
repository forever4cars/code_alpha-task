import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

# --- FAQs dataset ---
faqs = {
    "What is the return policy?": "You can return any product within 30 days of purchase.",
    "How long does delivery take?": "Delivery usually takes 3–5 business days.",
    "Do you offer international shipping?": "Yes, we ship to over 40 countries worldwide.",
    "What payment methods are accepted?": "We accept UPI, credit/debit cards, and net banking.",
    "How do I track my order?": "You can track your order through the tracking link sent to your email."
}

questions = list(faqs.keys())
answers = list(faqs.values())

# --- Preprocessing and vectorizing ---
stop_words = stopwords.words('english')

vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = vectorizer.fit_transform(questions)

def get_answer(user_query):
    user_tfidf = vectorizer.transform([user_query])
    similarity = cosine_similarity(user_tfidf, tfidf_matrix)

    index = similarity.argmax()  # best match
    score = similarity[0][index]

    if score < 0.3:   # threshold for poor match
        return "Sorry, I couldn't understand your question. Please try rephrasing."

    return answers[index]
print("FAQ Chatbot. Ask your questions! (Type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = get_answer(user_input)
    print("Chatbot:", response)

import tkinter as tk

def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_text + "\n")

    response = get_answer(user_text)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x500")

chat_box = tk.Text(root, height=25, width=60)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()
