from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime

app = Flask(__name__)

# Replace these with your Telegram bot token and chat ID
TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''

def send_to_telegram(name, email, phone):
    message = (
        f"📩 <b>New Contact Form Submission</b>\n\n"
        f"🕒 <b>Timestamp:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"👤 <b>Name:</b> {name}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📞 <b>Phone:</b> {phone}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        
        send_to_telegram(name, email, phone)


        return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
