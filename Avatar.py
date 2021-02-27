#Apart from the Must.py, here is the avatar command

@client.command()
async def avatar(ctx, member: discord.Member = None):         #so here if no arguemnt is passed, the avatar of the user is shown! 
    if not member:
        member = ctx.message.author
    show_avatar = discord.Embed(description="[Here's the avatar](%s)" %
                                member.avatar_url)
    show_avatar.set_image(url="{}".format(member.avatar_url))
    show_avatar.set_footer(text=f'{member}')
    print(member.avatar_url)
    await ctx.send(embed=show_avatar)
