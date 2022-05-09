import pypure


class Core(sys.modules[__name__].__class__):

    def init(self, config=True, config_path=f"{os.getcwd()}/pure.ini"):
        """Initializes pypure and it's components"""

        # Initializing pygame
        self.pygame = __import__("pygame")
        self.pygame.init()

    def quit(self):
        """Uninitializes and resets pypure"""


# Override the core module
sys.modules[__name__].__class__ = Core
