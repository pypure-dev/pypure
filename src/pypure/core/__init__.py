import os
import pypure

from configparser import ConfigParser


class Core(sys.modules[__name__].__class__):
    pygame = sys.modules[__name__].__class__("pygame")
    config = ConfigParser()
    config.user = None
    config.default = f"{os.path.dirname(__file__)}/pure.ini"

    def init(self, config=True, config_path=f"{os.getcwd()}/pure.ini"):
        """Initializes pypure and it's components"""

        # Initializing pygame
        self.pygame = __import__("pygame")
        self.pygame.init()

    def quit(self):
        """Uninitializes and resets pypure"""

        # Uninitializing pygame
        self.pygame.quit()

        # Resetting core
        self = self.__class__(__name__)


# Override the core module
sys.modules[__name__].__class__ = Core
