import random
from typing import Literal, Optional

import discord
from redbot.core import commands
from redbot.core.bot import Red

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]

class Stoned(commands.Cog):
    """How stoned are you?"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stoned(self, ctx: commands.Context, member: Optional[discord.Member]):
        """Check how stoned you are."""
        member = member or ctx.author
        random.seed(member.id + self.bot.user.id)
        if await self.bot.is_owner(member):
            buzz = random.randint(90, 100)
        else:
            buzz = random.randint(-10, 90)
        if buzz >= 160:
            emoji = self.bot.get_emoji(758821860972036106) or "<:weed:954756437584781332>"
        elif buzz >= 100:
            emoji = self.bot.get_emoji(758821993768026142) or "🤯"
        else:
            emoji = self.bot.get_emoji(758821971319586838) or "😔"
        await ctx.send(
            f"{member.mention} is {buzz}/100 stoned {emoji}",
            allowed_mentions=discord.AllowedMentions(users=False),
        )