import json
import requests
import html

urls = open("urls.txt").read().splitlines()
prod_ids = []

for i, u in enumerate(urls):
    r = requests.post("https://www.netcup.de/api/eggs", {"requrl": u})
    response_json = json.loads(r.content)
    if response_json["eggs"]:
        egg = response_json["eggs"][0]
        if egg["product_id"] not in prod_ids:
            prod_ids.append(egg["product_id"])
            print(f"-> {html.unescape(egg['title'])} ({html.unescape(egg['price'])})")
            print(f"      https://www.netcup.de{u}")
            print(
                f"      https://www.netcup.de/bestellen/produkt.php?produkt={egg['product_id']}&hiddenkey={egg['product_key']}"
            )
print(f"Done. {len(prod_ids)} eggs on {len(urls)} URLs found")
