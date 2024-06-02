from pyrogram import Client
from pyrogram import filters

# main daryoush
api_id =12345 
api_hash = 'fc393ce3063dsfasghadhadfgddgafdsfadsfdasfs'
bot_token = '54849465498:Adsagadfhgdsnarhadsfasdfasdf'



app = Client("my_account", api_id=api_id, api_hash=api_hash,  bot_token=bot_token)


@app.on_message(filters.all)
async def check_membership(client, message):

    await app.send_message(message.chat.id, "Hi there! I'm using **Pyrogram**") #Test message to connect to telegram api

    user_id = message.from_user.id  # ID The user who sent the command
    chat_id = "@laziz_Tv1"  # Replace with channel username

    try:
        member = await app.get_chat_member(chat_id, user_id)
        if member.status.name in['MEMBER', 'ADMINISTRATOR','OWNER']:
            await message.reply_text("You are a member of the channel.")

    except Exception as e:
        if "USER_NOT_PARTICIPANT" in str(e):
            await message.reply_text("You are not a member of the channel.")
        else:
            await message.reply_text(f"An error occurred: {e}")

app.run()

