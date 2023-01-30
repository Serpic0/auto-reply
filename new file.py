

import time

from telethon import TelegramClient, events
from telethon.tl.types import PeerUser
api_id = #go to https://my.telegram.org/auth to find out your api_id
api_hash = #go to https://my.telegram.org/auth to find out your api_hash

# fill in your own details here
phone = "your telegram number "  # (obligatory)
session_file = 'your telegram username'  # use your username (obligatory)


# content of the automatic reply
message = "any message"

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
