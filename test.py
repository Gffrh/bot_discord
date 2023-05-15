import discord 

intents = discord.Intents.all()

from discord.ext import commands

client = commands.Bot(command_prefix="!", intents = intents)

@client.command(name="del")
async def delete(ctx):
    messages = await ctx.channel.history(limit=10)

    for each_message in messages:
        await each_message.delete()

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_typing(channel, user, when):
     await channel.send(user.name+" is typing")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044900412551073832)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  message.content = message.content.lower()

  if message.content.startswith("salut"):
    await message.channel.send("wsh, ça dit quoi ?")
  await client.process_commands(message)


client.run("MTA5MTMzNTc1NDc4NzA3NDA5OA.G3z6nd.rI_N5URxaqJrV8MkdhlQXVxPgnbsN7OKtM8BoE")