from bs4 import BeautifulSoup as bs

with open("WAF24Attendees.html", "r") as f:
    html = f.read()

soup = bs(html, "html.parser")
links = soup.find_all("a")
profiles = [["Name", "Title", "Company", "Link"]]
base_url = "https://app.aviation-festival.com"

for link in links:
    spans = link.find_all("span")
    path = link.get("href")

    if len(spans) == 5 and len(spans[0].get_text()) == 2:
        profiles.append([
            spans[1].get_text(),
            "",
            spans[2].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) == 5 and len(spans[0].get_text()) != 2:
        profiles.append([
            spans[0].get_text(),
            spans[1].get_text().replace(",", " -"),
            spans[2].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) == 6:
        profiles.append([
            spans[1].get_text(),
            spans[2].get_text().replace(",", " -"),
            spans[3].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) == 7:
        profiles.append([
            spans[2].get_text(),
            spans[3].get_text().replace(",", " -"),
            spans[4].get_text().replace(",", " -"),
            base_url + path
        ])

with open("profiles.csv", "w") as f:
    for profile in profiles:
        f.write(",".join(profile) + "\n")
