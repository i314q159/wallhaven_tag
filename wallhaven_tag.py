import requests

WALLHAVEN_KEY = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
WALLHAVEN_TAG = "https://wallhaven.cc/api/v1/tag/"
WALLHAVEN_SEARCH = "https://wallhaven.cc/api/v1/search"


def wallhaven_json(wallhaven_api):
    return requests.get(wallhaven_api).json()


def wallhaven_tag_page(wallhaven_key, id):
    return f"{WALLHAVEN_SEARCH}?apikey={wallhaven_key}&q=id:{id}&page="


if __name__ == "__main__":
    img_paths = []
    tag_id = input("tag_id: ")
    wallhaven_tag_page = wallhaven_tag_page(WALLHAVEN_KEY, tag_id)

    tag_info = wallhaven_json(f"{WALLHAVEN_TAG}{tag_id}").get("data", None)
    match tag_info:
        case None:
            print("tag id is wrong")
        case _:
            tag_name = tag_info.get("name")
            last_page = (
                wallhaven_json(f"{wallhaven_tag_page}1").get("meta").get("last_page")
            )

            for page in range(1, last_page + 1):
                img_dict = wallhaven_json(f"{wallhaven_tag_page}{page}").get("data")
                for img in img_dict[0:]:
                    img_paths.append(img.get("path", None))
                print(f"page {page}")

            with open(f"./{tag_name}_{tag_id}.txt", "w") as f:
                f.writelines(img_path + "\n" for img_path in img_paths)

            print(f"{tag_name}_{tag_id}.txt, {len(img_paths)} line(s)")
