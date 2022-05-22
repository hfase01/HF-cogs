from typing import Optional

import discord
from redbot.core import commands
from redbot.core.bot import Red

from ..http import Button, ButtonStyle, Component, InteractionButton
from .button_menus import menu

class Buttons(commands.Cog):
    def __init__(self, bot: Red):
        self.bot = bot
