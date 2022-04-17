import json
import requests
import html
from urls import urls

prod_ids = []

for i, u in enumerate(urls):
	r = requests.post("https://www.netcup.de/api/eggs", {"requrl": u}).text
	response_json = json.loads(r)
	if response_json["eggs"]:
		egg = response_json["eggs"][0]
		if egg["product_id"] not in prod_ids:
			prod_ids.append(egg["product_id"])
			print(f"-> {html.unescape(egg['title'])} für {html.unescape(egg['price'])}")
			print(f"      Gefunden auf: https://netcup.de{u}")
			print(f"      https://www.netcup.de/bestellen/produkt.php?produkt={egg['product_id']}&hiddenkey={egg['product_key']}")
print("DONE!")
