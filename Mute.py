@bot.command(pass_context = True)
async def mute(ctx, user_id, userName: discord.User):
    if ctx.message.author.server_permissions.administrator:
        user = ctx.message.author
        role = discord.utils.get(user.server.roles, name="Muted")
        await client.add_roles(user, role)
     else:
       embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
       await bot.say(embed=embed)
