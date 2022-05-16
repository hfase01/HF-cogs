from redbot.core import commands

class Stoned(commands.Cog):
    """How stoned are you?"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stoned(self, ctx):
        """Check how stoned you are."""
        # Your code will go here
        await ctx.send("100/100 <:weed:954756437584781332>")