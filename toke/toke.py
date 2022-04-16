import contextlib
import re
from typing import Optional, Union

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import pagify

from .constants import emoji_dict, regionals

class tokey(commands.Cog):

    __author__ = ["hfase01"]
    __version__ = "0.0.1"

    @commands.command()
    async def toke(
        self, ctx: commands.Context, message: Optional[discord.Message]
    ) -> None:
        """
        React TOKEY to a message.
        `[message]` Can be a message ID from the current channel, a jump URL,
        or a channel_id-message_id from shift + copying ID on the message.
        """

        if message is None:
            async for messages in ctx.channel.history(limit=2):
                message = messages
        if not message.channel.permissions_for(ctx.me).add_reactions:
            return await ctx.send("I require add_reactions permission in that channel.")
        with contextlib.suppress(discord.HTTPException):
            for emoji in ("T", "O", "K", "E", "Y"):
                await message.add_reaction(emoji)
        if ctx.channel.permissions_for(ctx.me).manage_messages:
            await ctx.message.delete()
