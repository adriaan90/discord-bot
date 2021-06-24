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

    # Add preferred software roles
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

    # Add experience role    
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

    # Add major role
    if message_id == 857704738270478337:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        #Aerospace Engineering role
        if unicodedata.name(payload.emoji.name) == 'ROCKET':
            role = discord.utils.get(guild.roles, name="Aerospace Engineering")
        #Automotive Engineering role
        elif unicodedata.name(payload.emoji.name) == "ONCOMING POLICE CAR":
            role = discord.utils.get(guild.roles, name="Automotive Engineering")
        # Biomedical Engineering role
        elif unicodedata.name(payload.emoji.name) == "HOSPITAL":
            role = discord.utils.get(guild.roles, name="Biomedical Engineering")
        # Chemical Engineering role
        elif unicodedata.name(payload.emoji.name) == "LAB COAT":
            role = discord.utils.get(guild.roles, name="Chemical Engineering")
        # Civil Engineering role
        elif unicodedata.name(payload.emoji.name) == "TRAM CAR":
            role = discord.utils.get(guild.roles, name="Civil Engineering")
        # Computer Engineering role
        elif unicodedata.name(payload.emoji.name) == "PERSONAL COMPUTER":
            role = discord.utils.get(guild.roles, name="Computer Engineering")
        # Electrical Engineering role
        elif unicodedata.name(payload.emoji.name) == "HIGH VOLTAGE SIGN":
            role = discord.utils.get(guild.roles, name="Electrical Engineering")
        # Industrial Engineering role
        elif unicodedata.name(payload.emoji.name) == "HOUSE BUILDING":
            role = discord.utils.get(guild.roles, name="Industrial Engineering")
        # Mechanical Engineering role
        elif unicodedata.name(payload.emoji.name) == "WRENCH":
            role = discord.utils.get(guild.roles, name="Mechanical Engineering")
        # Mechatronics Engineering role
        elif unicodedata.name(payload.emoji.name) == "ROBOT FACE":
            role = discord.utils.get(guild.roles, name="Mechatronics Engineering")
        # Nuclear Engineering role
        elif unicodedata.name(payload.emoji.name) == "FACTORY":
            role = discord.utils.get(guild.roles, name="Nuclear Engineering")
        # Software Engineering role
        elif unicodedata.name(payload.emoji.name) == "VIDEO GAME":
            role = discord.utils.get(guild.roles, name="Software Engineering")
        # Structural Engineering role
        elif unicodedata.name(payload.emoji.name) == "CONSTRUCTION SIGN":
            role = discord.utils.get(guild.roles, name="Structural Engineering")    
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

    # Remove preferred software role
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

    # Remove education role
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

    # Remove major role
    if message_id == 857704738270478337:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        #Aerospace Engineering role
        if unicodedata.name(payload.emoji.name) == 'ROCKET':
            role = discord.utils.get(guild.roles, name="Aerospace Engineering")
        #Automotive Engineering role
        elif unicodedata.name(payload.emoji.name) == "ONCOMING POLICE CAR":
            role = discord.utils.get(guild.roles, name="Automotive Engineering")
        # Biomedical Engineering role
        elif unicodedata.name(payload.emoji.name) == "HOSPITAL":
            role = discord.utils.get(guild.roles, name="Biomedical Engineering")
        # Chemical Engineering role
        elif unicodedata.name(payload.emoji.name) == "LAB COAT":
            role = discord.utils.get(guild.roles, name="Chemical Engineering")
        # Civil Engineering role
        elif unicodedata.name(payload.emoji.name) == "TRAM CAR":
            role = discord.utils.get(guild.roles, name="Civil Engineering")
        # Computer Engineering role
        elif unicodedata.name(payload.emoji.name) == "PERSONAL COMPUTER":
            role = discord.utils.get(guild.roles, name="Computer Engineering")
        # Electrical Engineering role
        elif unicodedata.name(payload.emoji.name) == "HIGH VOLTAGE SIGN":
            role = discord.utils.get(guild.roles, name="Electrical Engineering")
        # Industrial Engineering role
        elif unicodedata.name(payload.emoji.name) == "HOUSE BUILDING":
            role = discord.utils.get(guild.roles, name="Industrial Engineering")
        # Mechanical Engineering role
        elif unicodedata.name(payload.emoji.name) == "WRENCH":
            role = discord.utils.get(guild.roles, name="Mechanical Engineering")
        # Mechatronics Engineering role
        elif unicodedata.name(payload.emoji.name) == "ROBOT FACE":
            role = discord.utils.get(guild.roles, name="Mechatronics Engineering")
        # Nuclear Engineering role
        elif unicodedata.name(payload.emoji.name) == "FACTORY":
            role = discord.utils.get(guild.roles, name="Nuclear Engineering")
        # Software Engineering role
        elif unicodedata.name(payload.emoji.name) == "VIDEO GAME":
            role = discord.utils.get(guild.roles, name="Software Engineering")
        # Structural Engineering role
        elif unicodedata.name(payload.emoji.name) == "CONSTRUCTION SIGN":
            role = discord.utils.get(guild.roles, name="Structural Engineering")    
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
