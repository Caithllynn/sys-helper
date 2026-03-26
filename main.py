from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8767002441:AAGUZ7q4IREEcfXQytvONe6WELak_blGLdQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "System ready."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()