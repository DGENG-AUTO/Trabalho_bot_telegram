import os

from dotenv import load_dotenv

from bot_telegram import BotTelegram

load_dotenv()
# 1) Renomeie o arquivo .env.example para .env
# 2) Adicione as chaves API das ferramentas utilizadas
token = os.getenv("TELEGRAM_BOT_TOKEN")
if not token:
    token = input("Digite seu token (Chave de acesso feito no BOTFather):")

bot_instance = BotTelegram(chave_api=token)
bot_instance.run()