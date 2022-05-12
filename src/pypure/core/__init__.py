import os
import pypure
import sys

from configparser import ConfigParser

# Used for setting global variables
__self__ = sys.modules[__name__]

# Variables
debug = None
pygame = sys.modules[__name__].__class__("pygame")
config = ConfigParser()
config.user = None
config.default = f"{os.path.dirname(__file__)}/pure.ini"


def init(
    config=True,
    config_path=config.default,
):
    """Initializes pypure and it's components"""

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
        __self__.config.read(__self__.config.default)  # Default configuration file
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


def quit():
    """Uninitializes and resets pypure"""

    # Uninitializing pygame
    __self__.pygame.quit()

    # Resetting core
    sys.modules[__name__] = __self__.__class__(__name__)
