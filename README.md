# Email-Bot
Python service that connects to an email inbox, triages unread messages, generates response, and triggers relevant workflows

## ✅ Features

- Connects to Gmail using IMAP
- Parses recnt unread messages
- Uses GPT (OpenAI) to generate context-aware replies
- Generates action items (e.g., access, maintenance requests)
- Sends email replies to tenants


## 🛠️ Setup Instructions

### 0. Prerequisites

- openAI account with API token
- gmail account with imap enabled
  - app password created for this google account


### 1. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root (based on sample.env):

```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_APP_PASS=your-app-password
OPENAI_API_KEY=your-openai-api-key
```

### 4. Run the App

```bash
python main.py
```
Action items are also written to a growing JSON file: `actions_log.json`


## ✨ Further Development:
- Add NLP intent classification for more accurate action item detection
- Add structured parsing of address from email text
- Implement action-item followup logic (see TODO)
- Integrate with real maintenance request systems
- Add error logging and retry/backoff logic
- Verbose unit testing

## 🧠 AI Tools Used
- **OpenAI gpt-3.5-turbo API**: To generate contextual replies from email bodies.
- ChatGPT as code assistant for:
  - inital boilder-plate
  - some parsing syntax
  - debugging
  - exploring various library options
- AI challenges:
  - getting chatGPT to understand the 'meta-prompting' for the agent API
  - leads to dilluted output quality as a result of being the extra degree of seperation 

## 🔧 Known Limitations

- Simple address parsing (not using NLP libraries like spaCy)
- No info retreval from extracted email context
  - See __TODO__ in `action_mamnager.py` for intended fast follow
- No tests included for brevity
- No retry for failed IMAP/SMTP connections