import requests

tag_id = input("tag_id: ")
api_key = "18nUEpLtkdrgmQpifc55Z1MAO8Cn7D44"
api_tag_info = "https://wallhaven.cc/api/v1/tag/"
api_tag_page = f"https://wallhaven.cc/api/v1/search?apikey={api_key}&q=id:{tag_id}&page="
img_paths = []

tag_name = requests.get(f"{api_tag_info}{tag_id}").json().get("data", None).get("name", None)

last_page = requests.get(f"{api_tag_page}1").json().get("meta", None).get("last_page", None)

for page in range(1, last_page + 1):
    img_dict = requests.get(f"{api_tag_page}{page}").json().get("data", None)

    for img in img_dict[0:]:
        img_paths.append(img.get("path", None))

with open(f"./{tag_name} {tag_id}.txt", "w") as f:
    for url in img_paths:
        f.write(f"{url}\n")

print(f"#{tag_name}_{tag_id}")
