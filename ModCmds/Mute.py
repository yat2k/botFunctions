# This function needs a role named "Muted" to work
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member = None):
    if not member:
        await ctx.send('Please choose a person you want to mute')
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.add_roles(role)
