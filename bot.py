import discord
from discord.ext import commands
from config import token

intents = discord.Intents.default()
intents.message_content = True
intents.attachments = True  # Eklerin işlenebilmesi için gerekli

client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yaptı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Komutları işle
    if message.content.startswith(client.command_prefix):
        await client.process_commands(message)
    else:
        if message.attachments:
            for attachment in message.attachments:
                if attachment.content_type and attachment.content_type.startswith('image/'):
                    await message.channel.send(f"Resim algılandı")
                else:
                    await message.channel.send("Bu resim değil.")

@client.command()
async def about(ctx):
    await ctx.send('Bu discord.py kütüphanesi ile oluşturulmuş echo-bot!')

@client.command()
async def info(ctx):
    await ctx.send('Merhaba! Bu bir örnek bot. Bot komutlarını kullanmak için / komutunu kullanabilirsin.')

@client.command()
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f"{num1} + {num2} = {result}")

client.run(token)
