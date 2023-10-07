# Discord bot import
import discord
from discord import app_commands
import os
from dotenv import load_dotenv

# Bot start
load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

guild_id = "your_guild_id (int)"

@client.event
async def on_ready():
    print("接続しました！")
    # await client.change_presence(activity=discord.Game(name="/help"))
    
    #スラッシュコマンドを同期
    await tree.sync()
    print("グローバルコマンド同期完了！")
    await tree.sync(guild=discord.Object(guild_id)) 
    print("ギルドコマンド同期完了！")

#Bot commands
# /test
@tree.command(name="test",description="テストコマンドです。")
async def send_add(interaction: discord.Interaction,text:str):
    await interaction.response.send_message(text, ephemeral=False)

# /test
@tree.command(name="test",description="テストコマンドです。")
@discord.app_commands.guilds(guild_id)
async def send_add(interaction: discord.Interaction,text:str):
    await interaction.response.send_message(text, ephemeral=False)

client.run(os.environ['token'])