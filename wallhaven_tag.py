import os

from wallhaven.api import Wallhaven

key = f"pRmbEacfPgeqeST5L2AH6qTEwxfN6SCO"


def init(api_key):
    wallhaven_obj = Wallhaven(api_key)
    return wallhaven_obj


def get_current_page(t_id, page):
    wallhaven.params["q"] = f"id:{t_id}"
    wallhaven.params["page"] = f"{page}"
    tag_info = wallhaven.search()

    current_page_data = tag_info.data
    meta = tag_info.meta
    print(f"current page: {meta.current_page}")

    if page == 1:
        last_page = meta.last_page
        name = meta.query.get("tag")

        return name, last_page, current_page_data
    else:
        return current_page_data


def get_full_url(wallpaper):
    wallpaper_id = wallpaper.id

    file_type = wallpaper.file_type.split("/")[1]
    wallpaper_file_type = f"jpg" if file_type == "jpeg" else file_type

    full_url = f"https://w.wallhaven.cc/full/{wallpaper_id[:2]}/wallhaven-{wallpaper_id}.{wallpaper_file_type}"
    return full_url


def get_urls(current_page_data, urls):
    for wallpaper in current_page_data:
        full_url = get_full_url(wallpaper=wallpaper)
        urls.append(full_url)


if __name__ == "__main__":
    tag_id = input("tag id: ")
    tag_urls = []

    wallhaven = init(api_key=key)

    tag_name, tag_last_page, first_page_data = get_current_page(t_id=tag_id, page=1)
    get_urls(current_page_data=first_page_data, urls=tag_urls)

    if tag_last_page != 1:
        for current_page in range(2, tag_last_page + 1):
            other_page_data = get_current_page(t_id=tag_id, page=current_page)
            get_urls(current_page_data=other_page_data, urls=tag_urls)

    file_path = os.path.join(".", f"{tag_name}_{tag_id}.txt")
    with open(file_path, "w") as f:
        f.writelines(f"{tag_url}\n" for tag_url in tag_urls)

    print(f"{tag_name}_{tag_id}.txt, {len(tag_urls)} line(s)")
