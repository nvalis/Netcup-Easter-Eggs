import requests
from bs4 import BeautifulSoup
import urllib

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0"
}


def write_urls_to_file(urls, output_file="urls.txt"):
    with open("urls.txt", "w") as of:
        of.write("\n".join(sorted(list(urls))))


def scrape_url(url):
    url = urllib.parse.urljoin("https://www.netcup.de/", url)
    print(f"Scraping {url} ...")
    r = requests.get(url, headers=headers)
    s = BeautifulSoup(r.content, features="lxml")
    hrefs = [a["href"] for a in s.find_all("a", href=True)]

    def interesting_url(url):
        return url.startswith("/") or url.startswith("https://www.netcup.de/")

    urls = set()
    for url in filter(interesting_url, hrefs):
        parsed_url = urllib.parse.urlparse(url)
        urls.add(parsed_url.path)
    return urls


scraped_urls = []
urls_to_scrape = {"/"}
all_urls = {"/"}

# now get all
while len(urls_to_scrape) > 0:
    current_url = urls_to_scrape.pop()
    if current_url in scraped_urls:
        continue
    urls = scrape_url(current_url)
    scraped_urls.append(current_url)
    all_urls = all_urls.union(urls)
    for url in list(urls):
        if url not in scraped_urls:
            urls_to_scrape.add(url)
    print(
        f"{len(all_urls)} collected, {len(scraped_urls)} scraped, {len(urls_to_scrape)} to scrape"
    )
    write_urls_to_file(all_urls)

print("Done.")
