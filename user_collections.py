import utils

config = utils.load_config()
KEY = config["wallhaven"]["key"]

proxy = utils.get_proxy(config)
wallhaven = utils.init(api_key=KEY, proxy=proxy)

collections = wallhaven.get_all_collections()

default_coll = next(c for c in collections if c.label == "Default")

default_coll_id = default_coll.id

listing = wallhaven.get_private_collection_listing(
    username="i314q159", collection_id=default_coll_id
)

# Download wallpapers.
# Listing is currently limited to the first 24 wallpapers.
for wallpaper in listing.data:
    print(wallpaper)
    wallpaper.save("./output/")

# TODO - 自己实现突破官方合集 24 张的限制
