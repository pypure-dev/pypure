import pypure


class Core(sys.modules[__name__].__class__):
    ...


# Override the core module
sys.modules[__name__].__class__ = Core
