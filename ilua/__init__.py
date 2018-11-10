# ILua
# Copyright (C) 2018  guysv

# This file is part of ILua which is released under GPLv2.
# See file LICENSE or go to https://www.gnu.org/licenses/gpl-2.0.txt
# for full license details.
import os.path
from .version import version as __version__

builtins_path = os.path.join(os.path.dirname(__file__), "builtins.lua")