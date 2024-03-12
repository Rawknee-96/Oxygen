import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
from core import Astroz, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
from utils.Tools import getConfig,getanti,getHacker

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antiemojid(Cog):
    def __init__(self, client:Astroz):
        self.client = client      
        self.headers = {"Authorization": f"Bot OTMxODE2Njk0Nzg2MTcwODkw.GkzHLL.7XEh31zCKnMRUmSxDIg6P4m-HMitx7zdWlJ-RE"}

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after) -> None:
      try:
        data = getConfig(guild.id)
        anti = getanti(guild.id)
        event= getHacker(guild.id)
        antievent = event["antinuke"]["antiemoji-delete"]
        punishment = data["punishment"]
        wled = data["whitelisted"]
        wlrole = data['wlrole']  
        wlroles = guild.get_role(wlrole)
        reason = "Deleting Emojis | Not Whitelisted"
        async for entry in guild.audit_logs(limit=1):
            user = entry.user.id
            hacker = guild.get_member(entry.user.id)
        api = random.randint(8,9)
        if user == self.client.user.id:
          pass
        elif entry.user == guild.owner:
          pass
        elif str(entry.user.id) in wled or anti == "off" or wlroles in hacker.roles or antievent == False:
            pass
        else:
         if entry.action == discord.AuditLogAction.emoji_delete:
           async with aiohttp.ClientSession(headers=self.headers) as session:
            if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    nme = before[0].name
                    img = await before[0].read()
                    await guild.create_custom_emoji(name=nme, image=img, reason=reason)
                    if r.status in (200, 201, 204):
                      
                      logging.info("Successfully banned %s" % (user))
            elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             nmee = before[0].name
                             imgg = await before[0].read()
                             await guild.create_custom_emoji(name=nmee, image=imgg, reason=reason)
                             if r2.status in (200, 201, 204):
                               
                               logging.info("Successfully kicked %s" % (user))
            elif punishment == "none":
              mem = guild.get_member(entry.user.id)
              await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
              nameme = before[0].name
              imagge = await before[0].read()
              await guild.create_custom_emoji(name=nameme, image=imagge, reason=reason)
            else:
                       return
      except Exception as error:
            if isinstance(error, discord.Forbidden):
              return