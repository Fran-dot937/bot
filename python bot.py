from telegram import Update, Chat
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# 🕘 Configurar horario de atención
HORA_INICIO = 7    # 7:00
HORA_FIN = 21      # 21:00

# Verifica si estamos dentro del horario permitido
def esta_en_horario():
    hora_actual = datetime.now().hour
    return HORA_INICIO <= hora_actual < HORA_FIN

# /start - Respuesta inicial
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hola! Aquest grup permet missatges de 07:00 a 21:00. Fora d'aquest horari estarà silenciat automàticament.")

# Mensajes normales
async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat

    if chat.type in [Chat.PRIVATE, Chat.GROUP, Chat.SUPERGROUP]:
        if esta_en_horario():
            await update.message.reply_text("✅ Gràcies pel teu missatge. Et respondré tan aviat com estigui disponible.")
        else:
            await update.message.reply_text("⛔ Fora d'horari. Estic actiu de 7:00 a 21:00.")

# Iniciar el bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("8017222143:AAEl9hTIQ0c5e5m8t8ZbMATeildDtIxKZU8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))

    print("🤖 Bot funcionando...")
    app.run_polling()