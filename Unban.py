#The below code unbans player
@client.command()
@commands.has_permissions(administrator = True) #admin/mod/any role you want :P
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
