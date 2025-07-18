# Email-Bot
Python service that connects to an email inbox, triages unread messages, generates response, and triggers relevant workflows

## ✅ Features

- Connects to Gmail using IMAP
- Parses unread messages
- Uses GPT (OpenAI) to generate context-aware replies
- Extracts action items (e.g., access, maintenance requests)
- Sends email replies to tenants
- Modular, testable architecture

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/domos-email-assistant.git
cd domos-email-assistant
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
OPENAI_API_KEY=your-openai-api-key
```


### 5. Run the App

```bash
python main.py
```

---

## 📄 Example Output

```
Reply:
Hi Wilkin, thanks for reaching out. We'll look into the toilet issue immediately. Once resolved, we’ll notify you and you can proceed with rent payment.

Action Items:
[
  {
    "type": "maintenance",
    "issue": "reported issue",
    "address": "parsed from email"
  }
]
```

Action items are also written to a growing JSON file: `actions_log.json`

---

### 🧪 Assumptions:
- Property and tenant data can be mocked or inferred from email body
- Email content is in English and follows loose structure
- One user account (property manager) per inbox

---

## 🔧 Known Limitations

- Simple address parsing (not using NLP libraries like spaCy)
- Action item logic is hardcoded and keyword-based
- No tests included for brevity
- No retry for failed IMAP/SMTP connections