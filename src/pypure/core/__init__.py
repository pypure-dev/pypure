import pypure


class Core(sys.modules[__name__].__class__):

    def init(self, config=True, config_path=f"{os.getcwd()}/pure.ini"):
        """Initializes pypure and it's components"""


# Override the core module
sys.modules[__name__].__class__ = Core
