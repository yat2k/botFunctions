@client.command(aliases=['make_role'])
@commands.has_permissions(manage_roles=True)
async def create_role(ctx, *, name):
	guild=ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created')
