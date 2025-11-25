🤖 FAQ Chatbot using NLP
(A smart FAQ-based chatbot built with Python, NLP, and Tkinter.)

📌 Overview

This project is a simple yet effective FAQ Chatbot that answers user questions by comparing input queries with a predefined FAQ dataset using NLP techniques such as TF-IDF vectorization and cosine similarity.

It also includes a Tkinter-based GUI, allowing users to interact with the chatbot through a clean and user-friendly interface.

This project was created as part of my internship at CodeAlpha, under the AI & ML domain.


✨ Features

🧠 NLP-powered question matching using TF-IDF
⚡ Real-time response generation
📚 Predefined FAQ dataset
❌ Handles unclear queries gracefully
💬 Interactive GUI chat window (Tkinter)
⌨️ Also supports command-line interaction 


🛠️ Technologies Used

Python 3.x
NLTK (tokenization, preprocessing)
Scikit-learn (TF-IDF, cosine similarity)
Tkinter (GUI interface)

📂 Project Structure
├── chatbot.py        # Main program containing NLP logic + GUI
└── README.md         # Documentation

🚀 How to Run the Project

1. Clone the Repository
git clone https://github.com/forever4cars/code_alpha-task
cd code_alpha-task

2. Install Dependencies
pip install nltk scikit-learn

3. Download NLTK Resources
The script automatically downloads them, but you can also run:
import nltk
nltk.download('punkt')
nltk.download('stopwords')

4. Run the Chatbot
python chatbot.py

💡 How It Works

The system stores a list of FAQs and their corresponding answers.
Each FAQ question is transformed into a TF-IDF vector.
When the user enters a query, the system:
Preprocesses and vectorizes the query
Calculates cosine similarity with all FAQ questions
Selects the closest match
If similarity is low (< 0.3), the chatbot says it cannot understand.
Otherwise, it returns the best possible answer.

🖥️ GUI Preview (Tkinter)

The application window includes:
A chat display box
A text entry field
A "Send" button

🧑‍💻 Author

Kartik Soma
Intern:CodeAlpha (AI & ML Domain)

📜 License

This project is open-source and available under the MIT License.
