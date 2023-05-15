import discord 
import datetime
intents = discord.Intents.all()

from discord.ext import commands

client = commands.Bot(command_prefix="!", intents = intents)


@client.event
async def on_ready():
    print("Le bot est prêt !")

last_commands = {}

@client.command(name ="last_command")
async def history(ctx):
    if ctx.author.id not in last_commands:
        await ctx.send("Vous n'avez pas encore entré de commandes.")
    else:
        await ctx.send("Voici les dernières commandes utilisées :")
        for command in last_commands[ctx.author.id]:
            await ctx.send(command)
@client.event
async def on_message(message):
    if message.content.startswith("!"):
        if message.author.id not in last_commands:
            last_commands[message.author.id] = []
        last_commands[message.author.id].append(message.content)

    await client.process_commands(message)


@client.command(name="heure")
async def heure(ctx):
    now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)
    time_str = now.strftime("%Hh%M")
    await ctx.send(f"Il est {time_str} en France")

    now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=10)
    time_str = now.strftime("%Hh%M")
    await ctx.send(f"{time_str} en Australie")

    now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=-3)
    time_str = now.strftime("%Hh%M")
    await ctx.send(f"Et {time_str} au Brésil. Si l'heure recherchée n'est pas inscrite, allez sur google (:")


@client.command(name = "surprise")
async def image(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://www.leparisien.fr/resizer/mtyH_ZTbgSlgjP81wWXhAfWtyD0=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/Q6MTNENGOZGU3BR5OUEO2GNMOI.jpg")
    await ctx.send(embed=embed)


client.run("MTA5MTMzNTc1NDc4NzA3NDA5OA.GEruki.7Sc0OxfePzrFSmlZWdwLXr4CQp4P42mrvO9Fj4")