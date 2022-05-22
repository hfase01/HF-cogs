from .buttons import Buttons


async def setup(bot):
    cog = Buttons(bot)
    bot.add_cog(cog)