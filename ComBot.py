from telethon import TelegramClient, sync
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetAdminLogRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import InputChannel
from telethon.tl.types import ChannelAdminLogEventsFilter
from telethon.tl.types import InputUserSelf
from telethon.tl.types import InputUser
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.types import ChannelParticipantsSearch
import time
import codecs
import re

api_id = 1
api_hash = ''

client = TelegramClient('abc', api_id, api_hash)
client.start()


tt=open("userlist2.txt", "a+")
queryKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_participants = []
channel = str(input("Link to the group: "))
all_participants=[]
for key in queryKey:
    offset = 0
    limit = 1000
    while True:
        participants = client(GetParticipantsRequest(
            channel, ChannelParticipantsSearch(key), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        for user in participants.users:
            try:
                if re.findall(r"\b[a-zA-Z]", user.first_name)[0].lower() == key:
                    all_participants.append(user)
                    print(user.username)
                    print(len(all_participants))
                    if "None" not in user.username:
                        tt.write(user.username)
                        tt.write("\n")
                    
            except:
                pass

        offset += len(participants.users)
    



from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelBannedRights
from datetime import datetime, timedelta

rights = ChannelBannedRights(
    until_date=datetime.now() + timedelta(hours = 20),
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True
)
for i in tt:
    i = t.split('\n')
    i = i[0]
    
    client(EditBannedRequest(channel, i, rights))



    
