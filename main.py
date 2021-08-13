# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:31:32 2021

@author: Andrew
"""

import os

import discord
from discord.ext import commands

from notion.block.collection.common import NotionDate
from notion.client import NotionClient
from datetime import datetime

TOKEN = os.environ['DISCORD_TOKEN']
DB_ID = os.environ['NOTION_DATABASE_ID']
NOTION_TOKEN = os.environ['NOTION_TOKEN']

VALID_CHANNELS = ["support", "feedback-and-bugs"]
# could add check for ctx.message.guild later, if for some reason we're getting weird adds from our bot.
VALID_GUILDS = ["boardwalk", "mirror"]
# @todo: come back and add reactions later instead of messages

"""
utils
"""


def update_notion_row(data, tag, link, sender, priority):
    client = NotionClient(token_v2=NOTION_TOKEN)
    cv = client.get_collection_view(DB_ID)

    row = cv.collection.add_row()
    row.name = data
    row.tags = [tag]
    row.messageLink = link
    row.sender = sender
    row.status = ["not assigned"]
    row.priority = [priority]
    row.createdAt = NotionDate(datetime.now())


"""
main bot functions
"""

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(
        f'{bot.user} is connected'
    )


@bot.command(name='bug', help='saves bug request down to our notion board')
async def nine_nine(ctx):
    if str(ctx.message.channel) not in VALID_CHANNELS:
        response = "wrong channel, you can only make these requests in `#feedback and bugs`, instead of in: `#{}`".format(str(
            ctx.message.channel))
        await ctx.send(response)
        return

    response = "bug has been recorded, thanks @{}!".format(
        str(ctx.message.author))
    await ctx.send(response)

    parsed_message = str(ctx.message.content).split("!bug")[1].strip()
    try:
        update_notion_row(parsed_message, "bug", str(
            ctx.message.jump_url), str(ctx.message.author), "high")
    except:
        await ctx.send("Error, @andrew.i needs updating")


@bot.command(name='feature', help='saves the feature request down to our notion board')
async def nine_nine(ctx):
    if str(ctx.message.channel) not in VALID_CHANNELS:
        response = "wrong channel, you can only make these requests in `#feedback-and-bugs`, instead of in: `#{}`".format(str(
            ctx.message.channel))
        await ctx.send(response)
        return

    response = "feature request has been recorded, thanks @{}!".format(
        str(ctx.message.author))
    await ctx.send(response)

    parsed_message = str(ctx.message.content).split("!feature")[1].strip()
    try:
        update_notion_row(parsed_message, "feature", str(
            ctx.message.jump_url), str(ctx.message.author), "low")
    except:
        await ctx.send("Error, @andrew.i needs updating")

bot.run(TOKEN)

# client is a lower level version of bot
# client = discord.Client()
# guild_name = "Boardwalk"

# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=guild_name)

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

#     # members = '\n - '.join([member.name for member in guild.members])
#     # print(f'Guild Members:\n - {members}')
