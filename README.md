# Assistente Multimídia no Telegram

Trabalho acadêmico desenvolvido para a disciplina **ENE140-2025.3-A — Programação para Engenharia**. O projeto implementa um bot do Telegram capaz de analisar imagens e arquivos de áudio enviados pelos usuários.

## Funcionalidades

- **Reconhecimento de imagens:** detecta e contabiliza objetos em imagens usando o modelo YOLOv8, apresentando os resultados em português.
- **Transcrição de áudio:** transcreve fala em português do Brasil.
- **Identificação de músicas:** tenta reconhecer músicas e fornece um link para ouvi-las no YouTube Music.
- **Menu interativo:** ao receber áudio ou mensagem de voz, o bot permite escolher entre transcrição e identificação musical.

## Tecnologias

- Python 3.12.8
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- SpeechRecognition, ShazamIO, yt-dlp e pydub
- FFmpeg para conversão de áudio

## Pré-requisitos

- Python **3.12.8**
- FFmpeg instalado e disponível no `PATH` do sistema
- Um bot do Telegram e seu token, criado pelo [BotFather](https://t.me/BotFather)
- Conexão com a internet para comunicação com o Telegram e os serviços de reconhecimento

## Instalação e execução

No terminal, a partir da pasta do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python main.py
```

Antes de executar, abra o `.env` e preencha as credenciais:

```dotenv
TELEGRAM_BOT_TOKEN=token_do_seu_bot
ACRCLOUD_ACCESS_KEY=sua_access_key
ACRCLOUD_ACCESS_SECRET=sua_access_secret
```

O token do Telegram também pode ser informado no terminal quando o programa pedir. As credenciais da ACRCloud são opcionais, mas sem elas essa alternativa de identificação musical não estará disponível. O arquivo `.env` é ignorado pelo Git; não o adicione ao repositório. Para desativar o ambiente virtual no Windows, use `deactivate`.

O bot permanece em execução enquanto o programa estiver aberto. Envie uma imagem para análise ou um áudio/nota de voz para escolher uma das opções disponíveis.

## Estrutura do projeto

| Arquivo | Descrição |
| --- | --- |
| `main.py` | Ponto de entrada; solicita o token e inicia o bot. |
| `bot_telegram.py` | Recebe mensagens, exibe as opções e coordena o processamento. |
| `bot_Imagem.py` | Detecta e contabiliza objetos em imagens com YOLOv8. |
| `speech_music_recognition.py` | Implementa transcrição e identificação de músicas. |
| `requirements.txt` | Lista as dependências Python do projeto. |
| `yolov8m.pt`, `yolov8n.pt` | Pesos dos modelos YOLO incluídos no repositório. |

## Observações

- O processamento de áudio depende do FFmpeg instalado e acessível pelo terminal.
- A transcrição utiliza o serviço de reconhecimento de fala do Google; a identificação musical pode consultar serviços externos.
- Arquivos de áudio e imagem enviados são baixados temporariamente para processamento e removidos ao final das rotinas correspondentes.
- Nunca publique tokens ou chaves de API no repositório. Antes de disponibilizar o código publicamente, verifique se as credenciais estão fora dos arquivos versionados e revogue/substitua qualquer chave que já tenha sido exposta.
- O arquivo `.env.example` contém apenas os nomes das variáveis. Copie-o para `.env` e coloque nele suas próprias credenciais; não preencha nem publique o exemplo com chaves reais.

## 📄 Licença

Esse código é autoral e cunho educativo, logo é distribuído sob a licença **MIT** (ajuste conforme sua preferência). 


## 👤 Autores

- **Ruan Baffa** — desenvolvimento do bot.
- **Artur Tafiri** — reconhecimento de imagens com YOLO.
- **Douglas** — reconhecimento de fala e música (`speech_music_recognition.py`).
- **Maria Vitória** — integração, testes e correções.

---

Projeto desenvolvido em conjunto como atividade da disciplina **ENE140-2025.3-A — Programação para Engenharia**.

