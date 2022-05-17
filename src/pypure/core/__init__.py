import os
import pypure
import sys

from configparser import ConfigParser
from pathlib import Path
from typing import Union

# Used for setting global variables
__self__ = sys.modules[__name__]

# Variables
debug = None
pygame = sys.modules[__name__].__class__("pygame")
config = ConfigParser()
config.user = None
config.default = f"{os.path.dirname(__file__)}/pure.ini"


def init(
    config: bool = True,
    config_path: Union[str, Path] = config.default,
) -> None:
    """Initializes pypure and it's components.

    Args:
        config: bool = True
            Tells if the config file should be used.
        config_path: Union[str, Path] = ...
            The config file path to be used.

    Returns:
        None

    Raises:
        None
    """

    # Correcting config parameter
    if not os.path.exists(config_path) and config:
        config = False

    # Reading configuration files
    if config:
        __self__.config.read([
            config_path,  # User's configuration file
            __self__.config.default,  # Default configuration file
        ])
    else:
        __self__.config.read(__self__.config.default)
        __self__.config.user = config_path

    # Applying configuration
    __self__.config.pure = __self__.config["pure"]
    __self__.config.pygame = __self__.config["tools.pygame"]

    __self__.debug = __self__.config.pure.getboolean("debug")
    pygame_support_prompt = __self__.config.pygame.getboolean("support_prompt")

    if not pygame_support_prompt:
        os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

    # Initializing pygame
    __self__.pygame = __import__("pygame")
    __self__.pygame.support_prompt = pygame_support_prompt
    __self__.pygame.init()

    from pygame import _sdl2 as SDL2
    __self__.pygame.SDL2 = SDL2

    # DEBUG
    if __self__.debug:
        print(f"[Pure] Version: {pypure.__version__}")
        print(f"[Pure] Config: {config}")


def quit() -> None:
    """Uninitializes pypure and it's components.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    # Uninitializing pygame
    __self__.pygame.quit()

    # Resetting core
    sys.modules[__name__] = __self__.__class__(__name__)


del Union
