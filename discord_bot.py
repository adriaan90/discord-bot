import discord
from discord.ext import commands
from secrets import *
from os import environ
import unicodedata


intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 841402767871442994:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added.")
            else:
                print("Member not found.")
        else:
            print("Role not found")
        
    if message_id == 844663014820806668:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if unicodedata.name(payload.emoji.name) == 'SCHOOL SATCHEL':
            role = discord.utils.get(guild.roles, name="High School")
        elif unicodedata.name(payload.emoji.name) == "GRADUATION CAP":
            role = discord.utils.get(guild.roles, name="Undergraduate")
        elif unicodedata.name(payload.emoji.name) == "SCHOOL":
            role = discord.utils.get(guild.roles, name="Graduate")
        elif unicodedata.name(payload.emoji.name) == "BOOKS":
            role = discord.utils.get(guild.roles, name="Postgraduate")
        elif unicodedata.name(payload.emoji.name) == "BRIEFCASE":
            role = discord.utils.get(guild.roles, name="Industry")
        else:
            role = None
        
        if role is not None:
            member = payload.member
            if member is not None:
                await member.add_roles(role)
                print("Role added.")
            else:
                print("Member not found.")
        else:
            print("Role not found")

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 841402767871442994:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed.")
            else:
                print("Member not found.")
        else:
            print("Role not found")

    if message_id == 844663014820806668:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if unicodedata.name(payload.emoji.name) == 'SCHOOL SATCHEL':
            role = discord.utils.get(guild.roles, name="High School")
        elif unicodedata.name(payload.emoji.name) == "GRADUATION CAP":
            role = discord.utils.get(guild.roles, name="Undergraduate")
        elif unicodedata.name(payload.emoji.name) == "SCHOOL":
            role = discord.utils.get(guild.roles, name="Graduate")
        elif unicodedata.name(payload.emoji.name) == "BOOKS":
            role = discord.utils.get(guild.roles, name="Postgraduate")
        elif unicodedata.name(payload.emoji.name) == "BRIEFCASE":
            role = discord.utils.get(guild.roles, name="Industry")
        else:
            role = None
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("Role removed.")
            else:
                print("Member not found.")
        else:
            print("Role not found")

if "TOKEN" in globals():
    client.run(TOKEN)
else:
    client.run(environ["TOKEN"])
