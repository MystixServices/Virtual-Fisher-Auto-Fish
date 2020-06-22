import discord
import json
import os
import asyncio
import colorama
from colorama import init, Fore

colorama.init()

from discord.ext import (
    commands,
    tasks
)

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')
autofish1 = config.get('autofish')

def startprint():

    if autofish1 == True:
        autofish = "Active"
    else:
        autofish = "Disabled"


    print(f'''{Fore.RESET}
     {Fore.CYAN}           ╔═╗╦╔═╗╦ ╦╔═╗╦═╗╔╦╗╔═╗╔╗╔
                ╠╣ ║╚═╗╠═╣║╣ ╠╦╝║║║╠═╣║║║
                ╚  ╩╚═╝╩ ╩╚═╝╩╚═╩ ╩╩ ╩╝╚╝{Fore.RESET}
                ╒◖══════════════════════◗╕
                 Made by: {Fore.RED}Vexy Development{Fore.RESET}
                {Fore.BLUE} [Auto-Fish] {Fore.RESET}| {autofish}
                {Fore.LIGHTGREEN_EX} [Auto-Verify]{Fore.RESET} | {Fore.LIGHTYELLOW_EX}Coming Soon {Fore.RESET}
                ╘◖══════════════════════◗╛
    ''' + Fore.RESET)




def Clear():
    os.system('cls')


Clear()


def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file" + Fore.RESET)
    else:
        token = config.get('token')
        try:
            Fisherman.run(token, bot=False, reconnect=True)
            os.system(f'title (Fisherman) - Vexy Development')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
            os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()



Fisherman = discord.Client()
Fisherman = commands.Bot(
    description='Fisherman',
    command_prefix=prefix,
    self_bot=True
)
Fisherman.remove_command('help')

@Fisherman.event
async def on_connect():
    Clear()
    await Fisherman.change_presence(activity=discord.Game("Virtual Fisher [Auto Fishing]"))

    if autofish1 == True:
        autofish = "Active"
    else:
        autofish = "Disabled"

    startprint()

@Fisherman.command(name='auto-fish', aliases=['fish'])
async def _auto_fish(ctx, channelid):  # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = Fisherman.get_channel(int(channelid))
            await channel.send('%fish')
            print(f'{Fore.BLUE}[AUTO-FISH] {Fore.GREEN}Fished: {count} many times' + Fore.RESET)
            await asyncio.sleep(3.8)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

if __name__ == '__main__':
    Init()
