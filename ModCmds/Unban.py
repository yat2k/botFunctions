#The below code unbans player
@client.command()
@commands.has_permissions(administrator = True) #admin/mod/any role you want :P
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    
    for ban_entry in banned_users:               #checks the banned user list and then compares with the argument and then unbans the player that matches :P
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}'
