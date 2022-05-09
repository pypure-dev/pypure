import os
import pypure


def test_init():
    config_path = f"{os.path.dirname(__file__)}/pure.ini"
    open(config_path, "x")

    # TRUE Testing
    if os.path.exists(config_path):
        os.remove(config_path)
    pypure.init(config=True, config_path=config_path)
    pypure.quit()

    open(config_path, "x")
    pypure.init(config=True, config_path=config_path)
    pypure.quit()

    # FALSE Testing
    pypure.init(config=False, config_path=config_path)
    pypure.quit()

    if os.path.exists(config_path):
        os.remove(config_path)
    pypure.init(config=False, config_path=config_path)
    pypure.quit()
