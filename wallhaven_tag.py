import requests

tag_id = input("tag_id: ")
wallhaven_key = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
wallhaven_tag_info = "https://wallhaven.cc/api/v1/tag/"
wallhaven_tag_page = f"https://wallhaven.cc/api/v1/search?apikey={wallhaven_key}&q=id:{tag_id}&page="
img_paths = []


def wallhaven_json(wallhaven_api):
    return requests.get(wallhaven_api).json()


tag_data = wallhaven_json(f"{wallhaven_tag_info}{tag_id}").get("data", None)

match tag_data:
    case None:
        tag_name = None
    case _:
        tag_name = tag_data.get("name", None)

match tag_name:
    case None:
        print("tag id is wrong")
    case _:
        last_page = wallhaven_json(f"{wallhaven_tag_page}1").get("meta", None).get("last_page", None)

        for page in range(1, last_page + 1):
            img_dict = wallhaven_json(f"{wallhaven_tag_page}{page}").get("data", None)

            for img in img_dict[0:]:
                img_paths.append(img.get("path", None))

        with open(f"./{tag_name} {tag_id}.txt", "w") as f:
            for url in img_paths:
                f.write(f"{url}\n")

        print(f"{tag_name}_{tag_id}.txt, {len(img_paths)} line(s)")
