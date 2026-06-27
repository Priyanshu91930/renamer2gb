import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27686895")
    API_HASH  = os.environ.get("API_HASH", "0e996bd3891969ec5dfebf8bb3e39e94")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8524209692:AAEJtw1VGTWYaCHiUYqxwb16Vcw9ip6SlkE")  
   
    # database config

    DATABASE_NAME = os.environ.get("DATABASE_NAME","anihubytrenamer")     
    DATABASE_URL  = os.environ.get("DATABASE_URL","mongodb+srv://anihubyt:Zxcvbnmm9193@cluster0.qv5tu12.mongodb.net/?appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/6e10888b69bdb2d235e81-e82f39fe8765f81d7e.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1246987713').split()]

    # channels logs
    FORCE_SUBS   = os.environ.get("FORCE_SUBS", "viralverse0909") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1004423517320"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))

    # Google Drive storage config — OAuth2 User Credentials
    # Run get_gdrive_token.py once to get these values
    GDRIVE_FOLDER_ID      = os.environ.get("GDRIVE_FOLDER_ID",      "1pdLfOTY9OohU_zV_UG6Mu9WJfwSp9NUP")
    GDRIVE_CLIENT_ID      = os.environ.get("GDRIVE_CLIENT_ID",      "")
    GDRIVE_CLIENT_SECRET  = os.environ.get("GDRIVE_CLIENT_SECRET",  "")
    GDRIVE_REFRESH_TOKEN  = os.environ.get("GDRIVE_REFRESH_TOKEN",  "")




class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @anihubyt"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/viralverse0909>anihubyt</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/viralverse0909>anihubyt</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://t.me/viralverse0909>Rename v4.7.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Contactmme_bot>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `anihubyt@upi`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @anihubyt</code>

💬 For Any Help Contact @viralverse0909
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
