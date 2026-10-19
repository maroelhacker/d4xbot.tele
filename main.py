import os
import telebot

# جلب التوكن الخاص بك من متغيرات البيئة
TOKEN = os.environ.get('8905176934:AAE8g8CRPh362m9TBdF4yd9spX-ul3jodOo')
bot = telebot.TeleBot(TOKEN)

# أمر /start بلمستك وحقوقك الخاصة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(
        message, 
        f"أهلاً بك يا {user_name}! 👋\n\n"
        f"🤖 هذا البوت خاص بي بالكامل ومطور بواسطة [اسمك هنا].\n"
        f"كيف يمكنني مساعدتك اليوم؟"
    )

# الرد التلقائي على أي رسالة
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"تم استقبال رسالتك: {message.text}")

if name == "main":
    print("البوت يعمل بكامل الحقوق...")
    bot.infinity_polling()
