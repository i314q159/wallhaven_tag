#!/usr/bin/env python3

import os
import sys

import requests

wallhaven_key = "pRmbEacfPgeqeST5L2AH6qTEwxfN6SCO"
wallhaven_tag = "https://wallhaven.cc/api/v1/tag/"
wallhaven_search = "https://wallhaven.cc/api/v1/search"


def wallhaven_json(wallhaven_api, default=None):
    r = requests.get(wallhaven_api)
    if r.status_code == requests.codes.ok:
        return r.json() or default


def wallhaven_tag_page(wallhaven_key, id):
    return f"{wallhaven_search}?apikey={wallhaven_key}&q=id:{id}&page="


if __name__ == "__main__":
    img_paths = []

    tag_id = sys.argv[1]
    wallhaven_tag_page = wallhaven_tag_page(wallhaven_key, tag_id)  # type: ignore

    try:
        tag_info = wallhaven_json(f"{wallhaven_tag}{tag_id}").get("data")  # type: ignore
        tag_name = tag_info.get("name")
        last_page = wallhaven_json(f"{wallhaven_tag_page}1").get("meta").get("last_page")  # type: ignore

        # TODO: async
        for page in range(1, last_page + 1):
            img_dict = wallhaven_json(f"{wallhaven_tag_page}{page}").get("data")  # type: ignore
            page_img_paths = [img.get("path", None) for img in img_dict]
            img_paths.extend(page_img_paths)
            print(f"page {page}")

        file_path = os.path.join(".", f"{tag_name}_{tag_id}.txt")

        with open(file_path, "w") as f:
            f.writelines(f"{img_path}\n" for img_path in img_paths)

        print(f"{tag_name}_{tag_id}.txt, {len(img_paths)} line(s)")

    except AttributeError:
        print("There is something wrong.")
        sys.exit()
