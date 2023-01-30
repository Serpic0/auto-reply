
TOKEN = "5949602059:AAG_UgLAUcyYczAGVdMdaAgDKWz0zV94myA"
import time

from telethon import TelegramClient, events
from telethon.tl.types import PeerUser
# sample API_ID from https://github.com/telegramdesktop/tdesktop/blob/f98fdeab3fb2ba6f55daf8481595f879729d1b84/Telegram/SourceFiles/config.h#L220
# or use your own
api_id = 22546322
api_hash = 'bde6ccdf91cf8a69adcb52674acb0df2'

# fill in your own details here
phone = "+998990137395"  # (obligatory)
session_file = 'muee_n'  # use your username (obligatory)


# content of the automatic reply
message = "Hello! I'm busy now. Will respond asap. If it is urgent, you can call me." \
          "\n Здравствуйте! я сейчас занят. Отвечу как только освобожусь. Если что-нибудь срочное, вы можете позвонить." \
          "\n Assalamu alaykum. Hozir men bandman. Boshashim bilan sizga javob beraman. Agarda muhim gap bolsa, qongiroq qilsangiz boladi."

if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            await client.get_input_entity(event.from_id)
            from_ = await event.client.get_entity(event.from_id)
            #my_user = await client.get_entity(PeerUser(id()))# this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')