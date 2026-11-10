import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Lê o token configurado nas variáveis de ambiente do Railway
TOKEN = os.getenv(9106050676:AAEcztx7wjoKU3vGR93nORpSfRYDfkHPkcM)
bot = telebot.TeleBot(9106050676:AAEcztx7wjoKU3vGR93nORpSfRYDfkHPkcM)

@bot.message_handler(commands=['/start', '/inf'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("🎬 Comprar Filmes de Demon Slayer", callback_data="comprar_filmes"),
        InlineKeyboardButton("ℹ️ Suporte e Ajuda", callback_data="ajuda")
    )
    
    texto = (
        "👋 **Bem-vindo à Deide Animes!**\n\n"
        "🎬 Aqui podes adquirir os filmes oficiais de *Demon Slayer* com alta qualidade.\n\n"
        "👇 Clica no botão abaixo para ver as opções e formas de pagamento:"
    )
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "comprar_filmes":
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("🇧🇷 Pix (Brasil) - R$ 5", callback_data="pagar_pix"),
            InlineKeyboardButton("🇦🇴 Multicaixa Express (Angola) - 2.000 Kz", callback_data="pagar_multicaixa")
        )
        texto = (
            "📦 **Conteúdo Disponível:**\n"
            "• Trilogia / Filmes de Demon Slayer\n"
            "• Qualidade: 1080p (Full HD) Legendado\n\n"
            "💳 **Escolhe o teu país / método de pagamento:**"
        )
        bot.edit_message_text(texto, call.message.chat.id, call.message.message_id, reply_markup=markup, parse_mode="Markdown")
        
    elif call.data == "pagar_pix":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "🇧🇷 **Pagamento via Pix (Brasil):**\n\n"
            "💰 **Valor:** R$ 5,00\n"
            "🔑 **Chave Pix:** `+550069056659`\n"
            "👤 **Beneficiário:** Adalberto \n\n"
            "📸 *Após o pagamento, envia o comprovativo aqui no chat para receberes o acesso imediato!*",
            parse_mode="Markdown"
        )
        
    elif call.data == "pagar_multicaixa":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "🇦🇴 **Pagamento via Multicaixa Express (Angola):**\n\n"
            "💰 **Valor:** 2.000 Kz\n"
            "📱 **Telemóvel:** `900 000 000`\n"
            "👤 **Beneficiário:** Deide Animes\n\n"
            "📸 *Após a transferência, envia a captura do talão aqui no chat para receberes o link de acesso!*",
            parse_mode="Markdown"
        )
        
    elif call.data == "ajuda":
        bot.answer_callback_query(call.id)
        bot.send_message(
            call.message.chat.id,
            "💬 Se tiveres alguma dúvida com o pagamento ou acesso aos filmes, envia mensagem."
        )

# Inicia o bot
if __name__ == '__main__':
    print("Bot a iniciar...")
    bot.infinity_polling()
