import tomllib

# https://github.com/lucasshiva/wallhaven
from wallhaven.api import Wallhaven
from wallhaven.session import handler


def load_config():
    with open("./config.toml", "rb") as f:
        return tomllib.load(f)


def get_proxy(config):
    proxy = config["proxy"]
    return f"http://{proxy['ip']}:{proxy['port']}"


def init(api_key, proxy):
    handler.session.proxies.update({"http": proxy, "https": proxy})
    wallhaven_obj = Wallhaven(api_key)
    return wallhaven_obj
