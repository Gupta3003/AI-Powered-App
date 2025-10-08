# 🤖 AI-QA Chatbot

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![HuggingFace](https://img.shields.io/badge/HuggingFace-API-orange.svg)](https://huggingfaceco/)

A smart and interactive AI-powered chatbot web application built with **Flask**, capable of answering user questions using the **Hugging Face OpenAI-compatible API**. This project features a clean and responsive UI, conversation memory, and real-time chat-like interface.

---

## **Demo Screenshot**
![Demo Screenshot](screenshots/demo.png)  
*(Optional: Add your screenshot in `screenshots/` folder)*

---

## **Features**
- Modern **chat interface** with user/bot bubbles  
- **Multi-turn conversation** using Flask sessions  
- **Responsive design** with separate CSS for index & result pages  
- **JavaScript validation** for empty input & auto-scroll for conversation  
- Reset conversation anytime  
- Supports **Hugging Face OpenAI-compatible models**  
- Easy to customize UI colors, fonts, and chat bubbles
---

## **Technologies Used**
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** Hugging Face OpenAI-compatible models (`zai-org/GLM-4.6:novita`)
- **Environment Variables:** `.env` file for API keys
- **Session Management:** Flask sessions to maintain conversation memory

---

## **Folder Structure**
```
ai_qa_bot/
├── app.py
├── templates/
│ ├── index.html
│ └── result.html
├── static/
│ ├── css/
│ │ ├── index.css
│ │ └── result.css
│ └── js/
│ ├── index.js
│ └── result.js
├── .env
├── requirements.txt
└── README.md
```

## **Installation & Setup**

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-qa-chatbot.git
cd ai-qa-
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3.**Install dependencies**
```bash
pip install -r requirements.txt
```

4.**Create a .env file**
```bash
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
```

5.**Run the Flask app**
```bash
python app.py
```

6.**Open in browser**
```bash
http://127.0.0.1:5000/
```

# Usage
- Go to the home page (index.html)
- Type your question in the input field
- Click Send
- View the AI response in result.html
- Click Reset Conversation to start fresh

## Example Conversation

| User                     | AI-Bot                                                                 |
|--------------------------|------------------------------------------------------------------------|
| What is Python?          | Python is a high-level, interpreted programming language designed for readability and versatility. |
| Who created Python?      | Python was created by **Guido van Rossum** in 1991.                   |
| What is Flask?           | Flask is a lightweight Python web framework used to build web applications. |
| How does the chatbot work?| The chatbot uses Hugging Face's OpenAI-compatible API to generate AI responses. |
| Can it remember context? | Yes, it maintains conversation memory using Flask sessions.            |
                  |

## Future Improvements
- Real-time **single-page chat** using AJAX or WebSockets
- **Voice input/output** for accessibility
- **User authentication** to save individual chat histories
- Deploy on **Heroku / AWS / Streamlit** for global access

---

## FAQ

**Q:** Can I use other Hugging Face models?  
**A:** Yes, simply replace the `MODEL_NAME` variable in `app.py`.

**Q:** How is the conversation stored?  
**A:** Using Flask `session`, so each user has a temporary chat memory.

**Q:** Can I style the chat interface?  
**A:** Yes, edit the CSS files in `static/css/` for custom design.

---

## Contributing
1. Fork the repository  
2. Create your branch (`git checkout -b feature/new-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/new-feature`)  
5. Open a Pull Request

---

## License
This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## Credits
- Built by [Your Name]  
- Powered by **Hugging Face OpenAI-compatible API**  
- Inspired by modern chat applications




