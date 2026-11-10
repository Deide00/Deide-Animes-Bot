import telebot

# O Token é lido automaticamente de forma segura pelo Railway
import os
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

# Mensagem inicial /start
@bot.message_handler(commands=['start', 'help'])
bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    texto = (
        "🎬 **Bem-vindo à Deide Animes!**\n\n"
        "🔥 Filme disponível: **Demon Slayer: Castelo Infinito** (CAM)\n\n"
        "💰 **Preços:**\n"
        "🇧🇷 Brasil (Pix): R$ 5,00\n"
        "🇦🇴 Angola (Multicaixa Express): 3.500 Kz\n\n"
        "Escolha a sua região para ver os dados de pagamento:"
    )
    
    # Criar botões interativos
    markup = telebot.types.InlineKeyboardMarkup()
    btn_br = telebot.types.InlineKeyboardButton("🇧🇷 Brasil (Pix)", callback_data="brasil")
    btn_ao = telebot.types.InlineKeyboardButton("🇦🇴 Angola (Multicaixa)", callback_data="angola")
    markup.add(btn_br, btn_ao)
    
    bot.send_message(message.chat.id, texto, reply_markup=markup, parse_mode="Markdown")

# Resposta ao clicar nos botões
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "brasil":
        resposta = (
            "🇧🇷 **Pagamento via Pix (Brasil):**\n\n"
            "Chave Pix (E-mail): `exemplo@email.com`\n"
            "Valor: **R$ 5,00**\n\n"
            "📸 Envie o comprovativo aqui no chat para receber o filme imediatamente!"
        )
    elif call.data == "angola":
        resposta = (
            "🇦🇴 **Pagamento via Multicaixa Express (Angola):**\n\n"
            "Telemóvel: `+244 900 000 000`\n"
            "Valor: **2.000 Kz**\n\n"
            "📸 Envie o talão do Multicaixa Express aqui no chat para receber o filme!"
        )
    
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, resposta, parse_mode="Markdown")

# Iniciar o bot
print("Bot a funcionar...")
bot.infinity_polling()
