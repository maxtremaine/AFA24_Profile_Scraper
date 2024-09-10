from bs4 import BeautifulSoup as bs

base_url = "https://app.aviation-festival.com"

with open("WAF24Attendees.html", "r") as f:
    html = f.read()

soup = bs(html, "html.parser")
links = soup.find_all("a")

profile_lengths = set()
profiles = [["Name", "Title", "Company", "Link"]]

for link in links:
    spans = link.find_all("span")
    path = link.get("href")
    profile_lengths.add(len(spans))

    if len(spans) is 5 and len(spans[0].get_text()) is 2:
        profiles.append([
            spans[1].get_text(),
            "",
            spans[2].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) is 5 and len(spans[0].get_text()) is not 2:
        profiles.append([
            spans[0].get_text(),
            spans[1].get_text().replace(",", " -"),
            spans[2].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) is 6:
        profiles.append([
            spans[1].get_text(),
            spans[2].get_text().replace(",", " -"),
            spans[3].get_text().replace(",", " -"),
            base_url + path
        ])

    if len(spans) is 7:
        profiles.append([
            spans[2].get_text(),
            spans[3].get_text().replace(",", " -"),
            spans[4].get_text().replace(",", " -"),
            base_url + path
        ])

with open("profiles.csv", "w") as f:
    for profile in profiles:
        f.write(",".join(profile) + "\n")
