# whatsappagent
To build an intelligent automation tool that fetches the latest news from various trusted sources and delivers them directly to a user's WhatsApp via the UltraMsg API. This project ensures users stay informed in real time, without needing to open news apps or websites.
Absolutely! Here's a clean and professional **README.md description** for your GitHub project: **AI WhatsApp News Bot**.

---

````markdown
# 📰 AI WhatsApp News Bot

An automated Python bot that fetches the latest news from NewsAPI and delivers it directly to your WhatsApp using UltraMsg API.

---

## 🔍 Features

- 📡 Fetches live news headlines (configurable by topic or country)
- 💬 Sends messages directly to your WhatsApp number via UltraMsg
- 📅 Easy to automate (daily/hourly scheduling supported)
- ⚙️ Fully customizable – news count, language, and filters
- 🧪 Works with free tiers of both NewsAPI and UltraMsg

---

## 🚀 How It Works

1. Sends a GET request to **NewsAPI** for the latest headlines.
2. Formats the response into a readable WhatsApp message.
3. Sends the message to your configured number using **UltraMsg** API.

---

## 🔧 Setup Instructions

### 1. Clone this Repository

```bash
git clone https://github.com/yourusername/ai-whatsapp-news-bot.git
cd ai-whatsapp-news-bot
````

### 2. Install Requirements

```bash
pip install requests
```

### 3. Configure the Keys

Open the script and replace:

```python
NEWS_API_KEY = "your_newsapi_key"
ULTRAMSG_INSTANCE_ID = "your_ultramsg_instance_id"
ULTRAMSG_TOKEN = "your_ultramsg_token"
TO_PHONE_NUMBER = "91xxxxxxxxxx"  # Your WhatsApp number without '+'
```

### 4. Run the Bot

```bash
python main.py
```

Or, run it in **Google Colab** for quick setup.

---

## 📄 Example Output

```
🗞️ Latest News Headlines:

1. OpenAI launches GPT-5 model.
https://techcrunch.com/...

2. India's space agency announces new Mars mission.
https://bbc.com/...

3. Apple unveils the Vision Pro 2.
https://verge.com/...
```

---

## 🛠 Customize

You can easily modify:

* Number of articles (`NUM_ARTICLES`)
* Country (`country=in`)
* Query terms (`q=technology`)
* Language (`language=en`)

---

## 📅 Automation (Optional)

Use services like:

* [Replit Scheduler](https://docs.replit.com/)
* [PythonAnywhere](https://www.pythonanywhere.com/)
* CRON Jobs (Linux/Mac)

---

## 📚 Credits

* [NewsAPI.org](https://newsapi.org)
* [UltraMsg WhatsApp API](https://ultramsg.com)

---

## 📜 License

This project is licensed under the MIT License.


