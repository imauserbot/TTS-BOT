#jack
import os
import pyrogram

from pyromod import listen
from pyrogram import filters, Client
from pyrogram.types import ForceReply
from gtts import gTTS
from gtts.lang import tts_langs

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
   
tts = Client(
    "text to speech bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN,
)

lang =   '''"af": "Afrikaans",
  "ar": "Arabic",
  "bn": "Bengali",
  "bs": "Bosnian",
  "ca": "Catalan",
  "cs": "Czech",
  "cy": "Welsh",
  "da": "Danish",
  "de": "German",
  "el": "Greek",
  "en": "English",
  "eo": "Esperanto",
  "es": "Spanish",
  "et": "Estonian",
  "fi": "Finnish",
  "fr": "French",
  "gu": "Gujarati",
  "hi": "Hindi",
  "hr": "Croatian",
  "hu": "Hungarian",
  "hy": "Armenian",
  "id": "Indonesian",
  "is": "Icelandic",
  "it": "Italian",
  "ja": "Japanese",
  "jw": "Javanese",
  "km": "Khmer",
  "kn": "Kannada",
  "ko": "Korean",
  "la": "Latin",
  "lv": "Latvian",
  "mk": "Macedonian",
  "ml": "Malayalam",
  "mr": "Marathi",
  "my": "Myanmar (Burmese)",
  "ne": "Nepali",
  "nl": "Dutch",
  "no": "Norwegian",
  "pl": "Polish",
  "pt": "Portuguese",
  "ro": "Romanian",
  "ru": "Russian",
  "si": "Sinhala",
  "sk": "Slovak",
  "sq": "Albanian",
  "sr": "Serbian",
  "su": "Sundanese",
  "sv": "Swedish",
  "sw": "Swahili",
  "ta": "Tamil",
  "te": "Telugu",
  "th": "Thai",
  "tl": "Filipino",
  "tr": "Turkish",
  "uk": "Ukrainian",
  "ur": "Urdu",
  "vi": "Vietnamese",
  "zh-CN": "Chinese",
  "zh-TW": "Chinese (Mandarin/Taiwan)",
  "zh": "Chinese (Mandarin)"'''


@tts.on_message(filters.command(["lang"]))
async def lang(client, message):
        await message.reply_text(
        text=f"Available languages and codes for them  :- \n {lang}")



@tts.on_message(filters.command(["start"]))
async def start(client, message):
        await message.reply_text(
        text=f"""**Hi {message.from_user.first_name},
An simple Text To speech bot**""")


@tts.on_message(filters.text & ~filters.reply)
async def texf(client, message):
           userid = str(message.chat.id)
           if not os.path.isdir(f"./DOWNLOADS/{userid}"):
              os.makedirs(f"./DOWNLOADS/{userid}") 

           language = await client.ask(
           message.chat.id,
           "**Plz enter an language code\n suppourt languages**[click here](https://www.google.com/url?sa=t&source=web&rct=j&url=https://cloud.google.com/text-to-speech/docs/voices&ved=2ahUKEwir4pPLlr7uAhWLwjgGHQAVAQAQFjACegQIDBAC&usg=AOvVaw3Q_9UBb0Xo-ljg87RGPX-8&cshid=1611821833928)",
           reply_markup=ForceReply(True),
        )  

           language_to_audio = language.text.lower()
           if language.text.lower() not in tts_langs():
            await message.reply_text(
             "```Unsupported Language Code.\n Use /lang command to see all available languages with their codes.```",
             quote=True,
             parse_mode="md"
        )
           else:
                 a = await message.reply_text(
                 "```processing```",
                   quote=True,
                   parse_mode="md"
           )
           new_file  = "./DOWNLOADS" + "/" + userid + "/" + "newaudio.mp3"
           myobj = gTTS(text=message.text, lang=language_to_audio, slow=False)   
           myobj.save(new_file)
           await message.reply_audio(new_file)
           await a.edit("**Thanks for using me**")

tts.run()
