import discord
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

client = discord.Client()
cli = MongoClient(os.getenv('MONGO'))
db = cli.heroku_zq5cdk49

bal = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511a')})
status = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511b')})
rqtype = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511c')})
rqdesc = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511d')})
rqserv = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511e')})
mess = db.doc.find_one({'_id': ObjectId('5d5779523f5cc0f1bdd8511f')})
typ = {}
version = "1.2.0"
 

@client.event
async def on_ready():
    guild = client.get_guild(469591475999604746)
    channel = client.get_channel(612112677166252050)
    await channel.send(f"""Bot started on **{version}**""")
    await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))


@client.event
async def on_member_join(member):
    guild = client.get_guild(469591475999604746)  # Blob-ify
    guild1 = client.get_guild(591038750273044501)  # Pixel Blob Central FLAG!
    if member.guild == guild:
        await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))
        channel = client.get_channel(469591475999604750)
        await channel.send(f"""<a:party:582383854262943745> Hey fellow **blob {member.mention}**, welcome to **Blob-ify**! You're the **{member.guild.member_count}th** blob to join our growing blob community! To get started, please check <#470303845495341057>. In order to request a blob, please check <#526232642425978892>. Have fun! <a:wumpusheart:582383394516631552>""")
    elif member.guild == guild1:
        channel = client.get_channel(591038750847533058)
        await channel.send(f"""<a:party:582383854262943745> Hey fellow **blob {member.mention}**, welcome to **{member.guild.name}**! You're the **{member.guild.member_count}th** blob to join our growing blob community! Have fun! <a:wumpusheart:582383394516631552>""")


@client.event
async def on_member_remove(member):
    guild = client.get_guild(469591475999604746)
    if member.guild == guild:
        await client.change_presence(activity=discord.Activity(name=f"""{guild.member_count} members""", type=discord.ActivityType.watching))


@client.event
async def on_message(message):
    guild = client.get_guild(469591475999604746)  # Blob-ify
    guild1 = client.get_guild(591038750273044501)  # Pixel Blob Central FLAG!
    lower = message.content.lower()
    if message.author.id not in typ.keys():
        typ[message.author.id] = 0
    if str(message.author) not in status.keys():
        status[str(message.author)] = 0
    if str(message.author) not in bal.keys():
        bal[str(message.author)] = 0
    if message.author.guild != guild:
        typ[message.author.id] = 0
    if lower == "cancel":
        if typ[message.author.id] > 0:
            await message.channel.send("**The requested action has been canceled.**")
            typ[message.author.id] = 0
            rqtype[str(message.author)], rqdesc[str(message.author)], rqserv[str(message.author)] = "", "", ""
    elif message.author.id == 292953664492929025:
        if "w.exc" in message.content:
            mem = message.content.split(" ")
            user = str(client.get_user(int(mem[1])))
            if user not in bal.keys():
                bal[user] = 0
            await message.channel.send("2 BLOB POINTS have been added to your account.")
            bal[user] += 2
            channel = client.get_channel(471878672677208084)
            await channel.send(f"""**Bank Update:** Bal of {user} now {bal[user]}""")
    else:
        if typ[message.author.id] == 0:
            if lower == "w.help":
                embed = discord.Embed(title="Blob Bot Help", description="The full list of W1Z4RD's commands")
                embed.add_field(name="w.request", value="Request a blob")
                embed.add_field(name="w.exchange", value="Exchange 2 BLOB POINTS for 500,000 BLOB COINS")
                embed.add_field(name="w.balance", value="Check your BLOB POINT balance")
                embed.add_field(name="w.req delete", value="Delete your current blob request")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                await message.channel.send(content=None, embed=embed)
            elif lower == "w.exchange":
                mem = str(message.author)
                if mem not in bal.keys():
                    bal[mem] = 0
                if bal[mem] > 1:
                    await message.channel.send("<@266319920009183242> will complete the transaction within 24 hours.")
                    bal[mem] -= 2
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {mem} now {bal[mem]}""")
                else:
                    await message.channel.send("You do not have enough BLOB POINTS to do so.")
            elif lower == "w.request":
                if status[str(message.author)] == 0:
                    embed = discord.Embed(title="W1Z Request Command", description="A full list of all blob types!")
                    embed.set_image(url="https://cdn.discordapp.com/attachments/470304317748805652/586383366538919965/d6783672-991f-4235-b3a6-b48b4d63eb5d.png")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                    embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                    await message.channel.send(content="__Please respond with the respective number, or say `cancel`__", embed=embed)
                    typ[message.author.id] += 1
                else:
                    await message.channel.send("You currently have a request in the queue. Either wait until the request is done or delete your request to request again. You can also choose to edit your request.")
            elif lower == "w.balance":
                await message.channel.send(f"""**Your Balance:** {bal[str(message.author)]} <:blobpoint:577932728033476611>""")
            elif lower == "w.bal":
                await message.channel.send(f"""**Your Balance:** {bal[str(message.author)]} <:blobpoint:577932728033476611>""")
            elif "w.say" in message.content:
                if message.author.id == 266319920009183242:
                    say = message.content.split(" ", 1)
                    await message.channel.send(f"""{say[1]}""")
                    await message.delete()
                if message.author.id == 538381052725428235:
                    say = message.content.split(" ", 1)
                    await message.channel.send(f"""{say[1]}""")
                    await message.delete()
                else:
                    await message.channel.send("You do not have the required permissions to use this command.")
            elif "w.add" in message.content:
                admin = guild.get_role(541658371913285632)
                if admin in message.author.roles:
                    say = message.content.split(" ", 2)
                    user = str(client.get_user(int(say[1])))
                    if user not in bal.keys():
                        bal[user] = 0
                    bal[user] += int(say[2])
                    await message.channel.send(f"""**{say[2]}bp** has/have been added to {user}'s balance""")
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {user} now {bal[user]}""")
                else:
                    await message.channel.send("You do not have the required permissions to use this command.")
            elif "w.remove" in message.content:
                admin = guild.get_role(541658371913285632)
                if admin in message.author.roles:
                    say = message.content.split(" ", 2)
                    user = str(client.get_user(int(say[1])))
                    if user not in bal.keys():
                        bal[user] = 0
                    bal[user] -= int(say[2])
                    await message.channel.send(f"""**{say[2]}bp** has/have been removed from {user}'s balance""")
                    channel = client.get_channel(471878672677208084)
                    await channel.send(f"""**Bank Update:** Bal of {user} now {bal[user]}""")
                else:
                    await message.channel.send("You do not have the required permissions to use this command.")
            elif lower == "w.emojiupdate":
                admin = guild.get_role(541658371913285632)
                admin1 = guild1.get_role(591039885583056947)  # FLAG
                if admin in message.author.roles:
                    channel = client.get_channel(578237505770618891)
                    async for message1 in channel.history():
                        await message1.delete()
                    for emoji in guild.emojis:
                        await channel.send(f"""{emoji} ~ `{emoji.name}`""")
                elif admin1 in message.author.roles:
                    channel = client.get_channel(591040559930671104)
                    async for message1 in channel.history():
                        await message1.delete()
                    for emoji in guild1.emojis:
                        await channel.send(f"""{emoji} ~ `{emoji.name}`""")
                else:
                    await message.channel.send("You do not have the required permissions to use this command.")
            elif "w.request " in message.content:
                if "delete" in message.content:
                    if status[message.author.id] > 0:
                        await message.channel.send("Are you sure you would like to delete your request? Your <:blobpoint:577932728033476611> will be refunded. Please `confirm` or `cancel`.")
                        typ[message.author.id] = 5
                    else:
                        message.channel.send("You currently have no active requests to delete.")
                elif "claim" in message.content:
                    print()
                elif "submit" in message.content:
                    print()
                elif "check" in message.content:
                    stat = status[str(message.author)]
                    if stat == 1:
                        print()
                else:
                    await message.channel.send("That was not a valid subcommand. Please see `w.help` for options.")
        elif typ[message.author.id] == 1:
            if "1" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Normal Blob"
                typ[message.author.id] += 1
            elif "2" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Animated Blob"
                typ[message.author.id] += 1
            elif "3" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Bongo Cat"
                typ[message.author.id] += 1
            elif "4" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Peep"
                typ[message.author.id] += 1
            elif "5" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Animated Peep"
                typ[message.author.id] += 1
            elif "6" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Full Blob Pack"
                typ[message.author.id] += 1
            elif "7" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Custom Emoji"
                typ[message.author.id] += 1
            elif "8" in message.content:
                await message.channel.send("__Great Choice! Now, please state what you would like your blob(s) to look like, or say `cancel`.__")
                rqtype[str(message.author)] = "Custom Emoji Pack"
                typ[message.author.id] += 1
            else:
                await message.channel.send("That was not a valid response. Send a number from 1 through 8.")
        elif typ[message.author.id] == 2:
            await message.channel.send("__Great! One last thing. Would you like this to be a server blob?__")
            await message.channel.send("Server blobs represent you in the server, and are made into emojis that you can use with Nitro.")
            await message.channel.send("However, only NORMAL BLOB requests can qualify. So what do you say, or `cancel`.")
            rqdesc[str(message.author)] = message.content
            typ[message.author.id] += 1
        elif typ[message.author.id] == 3:
            await message.channel.send("Cool! Now please confirm the following details before making your purchase.")
            await message.channel.send("The appropriate amount of BLOB POINTS will be deducted from your account as listed in <#526232642425978892>.")
            embed = discord.Embed(title="Confirm Information", description="Either `confirm` or `cancel`", color=0x0080c0)
            embed.add_field(name="Blob Type", value=rqtype[str(message.author)])
            embed.add_field(name="Blob Description", value=rqdesc[str(message.author)])
            embed.add_field(name="Server Blob?", value=message.content)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
            embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
            await message.channel.send(embed=embed)
            rqserv[str(message.author)] = message.content
            typ[message.author.id] += 1
        elif typ[message.author.id] == 4:
            if lower == "confirm":
                await message.channel.send("The blob request has been added to the queue.")
                await message.channel.send("You will receive notifications as your blob is being made.")
                await message.channel.send("Send any image references to <@266319920009183242>.")
                embed = discord.Embed(title=f"""{message.author}""")
                embed.add_field(name="Blob Type", value=rqtype[str(message.author)])
                embed.add_field(name="Blob Description", value=rqdesc[str(message.author)])
                embed.add_field(name="Server Blob?", value=rqserv[str(message.author)])
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/470304317748805652/581650589423763463/wiz.png")
                embed.set_footer(text=f"""Created by Tri#4823 ~ W1Z4RD {version}""")
                channel = client.get_channel(472560516133421077)
                await channel.send(content=f"""**Incoming Blob Request!** From {message.author.mention}""", embed=embed)
                typ[message.author.id] = 0
                status[message.author.id] = 1
            else:
                await message.channel.send("That was not a valid response. Please `confirm` or `cancel`.")
        elif typ[message.author.id] == 5:
            if lower == "confirm":
                await message.channel.send("<@266319920009183242> will proceed to delete your request and refund your <:blobpoint:577932728033476611>. At this point you may also start a new request.")
                status[message.author.id] = 0
            else:
                await message.channel.send("That was not a valid response. Please `confirm` or `cancel`.")

    # result = db.doc.update_one({"W1Z4RD#4341": 0}, bal)
    # print('Updated: {0}'.format(result.inserted_ids))

    dicts = [bal, status, rqtype, rqdesc, rqserv, mess]
    for d in dicts:
        db.doc.replace_one({'_id': d['_id']}, d, True)


@client.event
async def on_guild_emojis_update(guild0, before, after):
    channel = 0
    if guild0.id == 469591475999604746:
        channel = client.get_channel(570397486141669406)
    elif guild0.id == 591038750273044501:
        channel = client.get_channel(591040530331336789)  # FLAG
    emoadd, emoaddname, emoremove, emoremovename, lis, lis2 = "", "", "", "", [], []
    for emoji in before:
        for emoji2 in after:
            lis.append(emoji2.name)
        if emoji.name not in lis:
            emoremove = emoji
            emoremovename = emoji.name
    for emoji in after:
        for emoji2 in before:
            lis2.append(emoji2.name)
        if emoji.name not in lis2:
            emoadd = emoji
            emoaddname = emoji.name
    if emoremove == "":  # If no emoji was removed
        await channel.send(f"""<:w1:579473596041265152> **Added** {emoadd} `{emoaddname}`""")
    else:  # If an emoji was removed
        if emoadd == "":  # If an emoji was ONLY removed
            await channel.send(f"""<:w2:579473617134288898> **Removed** `{emoremovename}`""")
        else:  # If an emoji was renamed
            await channel.send(f"""<:w3:579473645706018827> {emoadd} **Renamed** `{emoremovename}` to `{emoaddname}`""")


client.run(os.getenv('TOKEN'))
