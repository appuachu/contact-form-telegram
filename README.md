Contact Form with Telegram Notification
This is a Flask-based Contact Form that automatically sends submissions to a Telegram bot using the Telegram API.

✨ Features
📩 Users can submit their name, email, and phone number.
🚀 The form data is sent to a Telegram bot instantly.
🔄 After submission, the user is redirected to a success page.
🔧 Simple and easy to set up using Flask and requests.
📌 How It Works
A user fills out the contact form and submits it.
The form data is sent to the Telegram bot using the Telegram API.
The user is redirected to a success page.

#🛠 Setup Instructions

#1️⃣ Prerequisites
Make sure you have Python 3 installed along with Flask.

#2️⃣ Clone the Repository
```bash
git clone https://github.com/appuachu/contact-form-telegram.git  
cd contact-form-telegram  
```
#3️⃣ Install Dependencies
```bash
pip install flask requests  
```
#4️⃣ Replace Telegram Credentials
Edit the app.py file and update the following:

Replace TELEGRAM_BOT_TOKEN with your bot's token.
Replace TELEGRAM_CHAT_ID with your chat ID.

#5️⃣ Run the Application
```bash
python app.py  
The app will start running at http://127.0.0.1:5000/
```
