#works for async and not for COGS!!

accept_decline = await ctx.send("Test")
cross = self.bot.get_emoji(558322190060093441)
checkM = self.bot.get_emoji(558322116685070378)
await accept_decline.add_reaction(checkM)
await accept_decline.add_reaction(cross)
