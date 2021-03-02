#The below code bans player
@client.command()
@commands.has_permissions(ban_members = True)        #make sure to not give it to everyone xD hehe
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

