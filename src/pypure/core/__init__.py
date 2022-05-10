import os
import pypure
import sys

from configparser import ConfigParser


class Core(sys.modules[__name__].__class__):
    debug = None
    pygame = sys.modules[__name__].__class__("pygame")
    config = ConfigParser()
    config.user = None
    config.default = f"{os.path.dirname(__file__)}/pure.ini"

    def init(self, config=True, config_path=f"{os.getcwd()}/pure.ini"):
        """Initializes pypure and it's components"""

        # Correcting config parameter
        if not os.path.exists(config_path) and config:
            config = False

        # Reading configuration files
        if config:
            self.config.read([
                config_path,  # User's configuration file
                self.config.default,  # Default configuration file
            ])
        else:
            self.config.read(self.config.default)  # Default configuration file
            self.config.user = config_path

        # Applying configuration
        self.config.pure = self.config["pure"]
        self.config.pygame = self.config["tools.pygame"]

        self.debug = self.config.pure.getboolean("debug")
        pygame_support_prompt = self.config.pygame.getboolean("support_prompt")

        if not pygame_support_prompt:
            os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

        # Initializing pygame
        self.pygame = __import__("pygame")
        self.pygame.support_prompt = pygame_support_prompt
        self.pygame.init()

        from pygame import _sdl2 as SDL2
        self.pygame.SDL2 = SDL2

        # DEBUG
        if self.debug:
            print(f"[Pure] Version: {pypure.__version__}")
            print(f"[Pure] Config: {config}")

    def quit(self):
        """Uninitializes and resets pypure"""

        # Uninitializing pygame
        self.pygame.quit()

        # Resetting core
        self = self.__class__(__name__)


# Override the core module
sys.modules[__name__].__class__ = Core
