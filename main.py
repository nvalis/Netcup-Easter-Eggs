import json
import requests
import html

urls = ["/",
"/ausbildung/",
"/ausbildung/bachelor-of-engineering-studiengang-informationstechnik-mwd",
"/ausbildung/fachinformatik-anwendungsentwicklung-mwd",
"/ausbildung/fachinformatik-systemintegration-mwd",
"/bestellen/agb.php",
"/bestellen/domainangebote.php",
"/bestellen/softwareangebote.php",
"/bestellen/warenkorb.php",
"/groupware/",
"/hosting/",
"/hosting/qualitaetsgarantien.php",
"/hosting/webhosting-application-hosting.php",
"/hosting/webhosting-testaccount.php",
"/jobs/",
"/jobs/junior-php-developer-mwd",
"/jobs/software-engineer-mwd-faoer-rd-go-python",
"/jobs/supportmitarbeiter-mwd",
"/jobs/systemadministrator-mit-fokus-auf-linux-und-3rd-level-support-mwd",
"/kontakt/",
"/kontakt/datenschutzerklaerung.php",
"/kontakt/impressum.php",
"/kontakt/postanschrift.php",
"/kontakt/telefonsupport.php",
"/professional/",
"/professional/dedizierte-server/",
"/professional/dedizierte-server/perc_raid_controller.php",
"/professional/dedizierte-server/remote_management.php",
"/professional/individuelle-loesungen/",
"/professional/individuelle-loesungen/penetrationtesting.php",
"/professional/individuelle-loesungen/preise.php",
"/professional/individuelle-loesungen/servermanagement.php",
"/professional/individuelle-loesungen/software-installationen.php",
"/professional/managed-server/managed-cloud-cluster.php",
"/professional/managed-server/managed-privateserver.php",
"/professional/managed-server/managed-server.php",
"/ssl-zertifikate/",
"/ssl-zertifikate/geotrust.php",
"/ssl-zertifikate/globe.php",
"/ssl-zertifikate/rapid.php",
"/ssl-zertifikate/thawte.php",
"/support/",
"/ueber-netcup/",
"/ueber-netcup/auszeichnungen.php",
"/ueber-netcup/ddos-schutz-filter.php",
"/ueber-netcup/hardware-infrastruktur.php",
"/ueber-netcup/kundenmeinungen-netcup.php",
"/ueber-netcup/merchandising.php",
"/ueber-netcup/oekostrom.php",
"/ueber-netcup/partner.php",
"/ueber-netcup/public-relations.php",
"/ueber-netcup/rechenzentrum.php",
"/ueber-netcup/referenzen.php",
"/vserver/",
"/vserver/reseller_angebote_vserver.php",
"/vserver/root-server-erweiterungen.php",
"/vserver/storagespace.php",
"/vserver/uebersicht_vserver_angebote.php",
"/vserver/vergleich-linux-vserver-kvm.php",
"/vserver/vergleich-root-server-vps.php",
"/vserver/vps.php",
"/vserver/vserver_guenstig_qualitaet.php",
"/vserver/vserver_images.php",
"/vserver/vstorage.php"
]

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
