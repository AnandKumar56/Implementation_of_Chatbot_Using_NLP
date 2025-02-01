# Implementation of Chatbot Using NLP 🤖

This project is an **intent-based chatbot** built using **Natural Language Processing (NLP)** and **Machine Learning (Logistic Regression)**. It uses `streamlit` for the UI and `scikit-learn` for intent classification.

---

## 🚀 Features
- Recognizes user **intents** using `TF-IDF` vectorization.
- Uses `Logistic Regression` for text classification.
- Supports **custom intents** from `intents.json`.
- Stores conversation history in `chat_log.csv`.
- Interactive **web interface** using `Streamlit`.

---

## 💁️ Folder Structure
```
📂 Implementation_of_Chatbot_Using_NLP
🌂🔖 app.py               # Main chatbot application
🌂🔖 intents.json         # Training data (intents and responses)
🌂🔖 chat_log.csv         # Conversation history
🌂🔖 requirements.txt     # Required dependencies
🌂🔖 README.md            # Project documentation
👈🏼 .venv                # Virtual environment (optional)
```

---

## 🛠️ Installation & Setup

### **1⃣ Clone the Repository**
```bash
git clone https://github.com/AnandKumar56/Implementation_of_Chatbot_Using_NLP.git
cd Implementation_of_Chatbot_Using_NLP
```

### **2⃣ Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv .venv
source .venv/bin/activate  # For Mac/Linux
.\.venv\Scripts\activate   # For Windows
```

### **3⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4⃣ Run the Chatbot**
```bash
streamlit run app.py
```

---

## 🔧 Usage
1. Open the **Streamlit interface** in your browser.
2. Enter a message in the **chatbox** and get a chatbot response.
3. The chatbot logs all conversations in `chat_log.csv`.
4. To customize responses, edit **`intents.json`**.

---

## 📝 Editing `intents.json`
To add new intents, modify `intents.json`:
```json
{
    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hello", "Hi", "Hey"],
            "responses": ["Hello!", "Hi there!"]
        }
    ]
}
```
Run the chatbot again after editing.

---

## 📌 Dependencies
- **Python** (>=3.8)
- `streamlit`
- `scikit-learn`
- `nltk`

Install using:
```bash
pip install streamlit scikit-learn nltk
```

---

## 🏆 Future Enhancements
- 🔥 Add **Deep Learning (Transformers) for better accuracy**
- 🌎 Deploy on **AWS/GCP/Heroku**
- 🎤 **Voice recognition** using Speech-to-Text

---

## 🤝 Contributing
1. **Fork** the repository.
2. **Create a branch** for your feature:  
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push the branch** and **Create a Pull Request**.


## 🎯 Author
Developed by **Anand Kumar Dalwaie**  
🔗 GitHub: [AnandKumar56](https://github.com/AnandKumar56)  

---

## 🚀 Show Your Support!
🌟 **Star this repo** if you found it useful!  
📲 Share with your friends and contribute!  
