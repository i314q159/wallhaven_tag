import utils

config = utils.load_config()
KEY = config["wallhaven"]["key"]

proxy = utils.get_proxy(config)
wallhaven = utils.init(api_key=KEY, proxy=proxy)

tag = wallhaven.get_tag(120)
print(tag)
