import json
import requests
import html
from urls import urls

for i, u in enumerate(urls):
  api = "https://www.netcup.de/api/eggs"
  data = {"requrl": u}
  response = requests.post(api, data).text
  response_json = json.loads(response)
  if response_json["eggs"] != False:
    print(f"{i+1}/{len(urls)}: ")
    print(f"-> {html.unescape(response_json['eggs'][0]['title'])} für {html.unescape(response_json['eggs'][0]['price'])}")
    print(f"      Gefunden auf: https://netcup.de{u}")
    print(f"      https://www.netcup.de/bestellen/produkt.php?produkt={response_json['eggs'][0]['product_id']}&hiddenkey={response_json['eggs'][0]['product_key']}")
print("DONE!")
