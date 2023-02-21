import random
import time

import requests

wallhaven_key = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
wallhaven_tag_info = "https://wallhaven.cc/api/v1/tag/"


def wallhaven_json(wallhaven_api):
    return requests.get(wallhaven_api).json()


def wallhaven_tag_page(wallhaven_key, tag_id):
    return f"https://wallhaven.cc/api/v1/search?apikey={wallhaven_key}&q=id:{tag_id}&page="


if __name__ == "__main__":
    img_paths = []
    tag_id = input("tag_id: ")
    wallhaven_tag_page = wallhaven_tag_page(wallhaven_key, tag_id)

    tag_data = wallhaven_json(f"{wallhaven_tag_info}{tag_id}").get("data", None)
    match tag_data:
        case None:
            print("tag id is wrong")
        case _:
            tag_name = tag_data.get("name")
            last_page = (
                wallhaven_json(f"{wallhaven_tag_page}1").get("meta").get("last_page")
            )

            for page in range(1, last_page + 1):
                img_dict = wallhaven_json(f"{wallhaven_tag_page}{page}").get("data")
                for img in img_dict[0:]:
                    img_paths.append(img.get("path", None))
                print(f"page {page}")
                time.sleep(random.random() * 3)

            with open(f"./{tag_name} {tag_id}.txt", "w") as f:
                f.writelines(img_path + "\n" for img_path in img_paths)

            print(f"{tag_name} {tag_id}.txt, {len(img_paths)} line(s)")
