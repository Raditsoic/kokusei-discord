from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
import requests as r
import json

class Responses(commands.Cog):
    def __init__(self, client):
        self.client = client
        load_dotenv()
        
    @commands.Cog.listener()
    async def on_ready(self):
        await print("Success: Response Cog is active...")
        
    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        bot_id = int(os.getenv('BOT_ID'))
        bot_name = os.getenv('BOT_NAME')
        print(message)
        if message.author.id != bot_id or message.author.name != bot_name:
            #print(dir(message))
            #print(type(message))
            print(message)
            #print(message.content)
            content = message.content
            bad_word = ['fuck', 'shit', 'bitch']
            for word in bad_word:
                if word in content:
                    ctx.send("Don't use bad word plss!!!")
                    
    @commands.Cog.listener()
    async def on_message(self, ctx, message):
        bot_id = int(os.getenv('BOT_ID'))
        bot_name = os.getenv('BOT_NAME')
        if message.author.id != bot_id or message.author.name != bot_name:
            content = message.content
            
    @commands.command()
    async def quotes(self, ctx):
        req = r.get("https://animechan.xyz/api/random")
        content = req.content.decode("utf-8")
        data = json.loads(content)
        embed = discord.Embed(title="Quotes", timestamp=ctx.message.created_at, color=discord.Color.light_grey())
        embed.add_field(name="", value=f"{data['quote']} - **{data['character']}**")
        embed.set_footer(text="Powered by Animechan")
        await ctx.send(embed=embed)        
        
async def setup(client):
    await client.add_cog(Responses(client))