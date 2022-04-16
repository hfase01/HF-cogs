import contextlib
import re
from typing import Optional, Union

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.utils.chat_formatting import pagify

from .constants import emoji_dict, regionals

