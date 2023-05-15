import discord 
import datetime
import requests
from historique import historique_commandes

History = historique_commandes

intents = discord.Intents.all()
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents = intents)

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.command(name="del")
async def delete(ctx):
    await ctx.channel.purge(limit=10)
    History.add_command("!del")


full_history = {}
@client.command(name ="full_history")
async def history(ctx):
    await ctx.send("Voici les dernières commandes utilisées :")
    for command in full_history[ctx.author.id]:
        await ctx.send(command)

@client.event
async def on_message(message):
    if message.content.startswith("!"):
        if message.author.id not in full_history:
            full_history[message.author.id] = []
        full_history[message.author.id].append(message.content)

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


@client.command(name= "surprise")
async def chien(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")

    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        embed = discord.Embed()
        embed.set_image(url=image_url)
        await ctx.send(embed=embed)
