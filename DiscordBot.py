import discord
from random import randint
import os


class MyCLient(discord.Client):

    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep Bop!")

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content == "!riddle" or message.content == "!Riddle":
            """satz_liste = ["Riddle du alter Haudegen!", "Gold war mal cool, aber nicht eternal....",
                          "The serpent dies but its soul is eternal...", "LeL I bims Riddle! " "Dracarys!"]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]"""
            gifs = ["riddle1.gif", "riddle2.gif", "riddle3.gif"]
            index = randint(0, len(gifs) - 1)
            text = gifs[index]
            await message.channel.send(file = discord.File(text))

        if message.content == "!dracarys" or message.content == "!Dracarys":
            gifs = ["dracarys.gif", "minidracarys.gif"]
            index = randint(0, len(gifs) - 1)
            text = gifs[index]
            await message.channel.send(file = discord.File(text))

        if message.content == "!hertha":
            satz_liste = ["Hier könnte Ihre Werbung stehen!", "Read Nine Star Hegemon Body Arts!", "You should try Overgeared!",
                          "May the bot grow! "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!chigga":
            satz_liste = ["Join Skylords with your whole family... or something like that...", "I am french and everyone should know! ",
                          "Mdrrrr", "One day i will be f2p! "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!pure" or message.content == "!pureluck":
            """satz_liste = ["My Panda is STRONK!!!", "Iskender Kebab ist beste! ", "Who wants some ruins? Too bad, those are mine.",
                          "I have apples for everyone. ", "Das Leben ist hart ohne Mastercard!"]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")"""
            gifs = ["pure1.gif", "pure2.gif", "pure3.gif"]
            index = randint(0, len(gifs) - 1)
            text = gifs[index]
            await message.channel.send(file = discord.File(text))

        if message.content == "!guiying" or message.content == "!Guiying":
            satz_liste = ["Ja ich spiele noch, aber Riddle ist bei uns....",
                          "Ying mein Name. GuiYing."]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!tanaka":
            satz_liste = ["HAHAHAHA I'm back! ", "What is all this? ", "Did I miss something? "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!cyro":
            satz_liste = ["Once upon a time I had beef with some people....", "Still second to ascend y'all.", "Why am I in the german role??? "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!deathrose":
            satz_liste = ["Casually playing 3 servers.", "You thought it was another deathrose but it was me DIO, oh wait, it was me DEATHROSE. ",
                          "This is french now. "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!affx":
            satz_liste = ["FRIED CHICKEN!!!", "Wow pure panda stronk. ", "Run! "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!chaos":
            await message.channel.send("`" + "Is it me or does it seem chaotic in here??" + "`")

        if message.content == "!jms":
            satz_liste = ["Only souls are eternal, not gold...", "Thinking and writing is really hard sometimes....",
                          "Ou sont les francais? "]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")

        if message.content == "!namige":
            satz_liste = ["We do it for the quest!!", "Thanks forthequestION. ", "Smething funny here..."]
            index = randint(0, len(satz_liste) - 1)
            text = satz_liste[index]
            await message.channel.send("`" + text + "`")


        if message.content == "!skylords":
            await message.channel.send("`" + "#noMoneySpent" + "`")

        if message.content == "!champion":
            await message.channel.send("`" + "#noMoneySpentlikeSkyLords" + "´")

        if message.content == "!eternalsouls":
            await message.channel.send("`" + "This is french now. " + "`")

        if message.content == "!forthequest":
            await message.channel.send("`" + "We have no answers FORTHEQUESTions." + "`")


client = MyCLient()
client.run(os.environ["TOKEN"])