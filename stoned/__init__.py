from .stoned import Stoned


async def setup(bot):
    cog = Stoned(bot)
    bot.add_cog(cog)