import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ⚠️ ВСТАВЬ свои данные сюда:
TOKEN = "8152710314:AAHKBtJ6aWyFVzmwaJ_zwxrCPNZrnRuSCuM"
CHAT_ID = "1508232520"
URL = "https://temas777.github.io/Tesy/"  # ссылка на мини-апп или сайт

bot = telegram.Bot(token=TOKEN)

keyboard = [
    [InlineKeyboardButton("✨ Открыть мини-апп", url=URL)]
]
reply_markup = InlineKeyboardMarkup(keyboard)

bot.send_message(chat_id=CHAT_ID, text="Запусти мини-апп:", reply_markup=reply_markup)
print("✅ Сообщение успешно отправлено!")
