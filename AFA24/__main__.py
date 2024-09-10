from bs4 import BeautifulSoup as bs

base_url = 'https://app.aviation-festival.com'

with open('AFAAirlineAttendees.html', 'r') as f:
    html = f.read()

soup = bs(html, 'html.parser')
links = soup.find_all('a')
profiles = [[ 'airline', 'title', 'name', 'url' ]] # Container for CSV

for link in links:
    content = link.find_all('span')

    # Escape anything that is not a profile
    if len(content) == 0:
        continue

    # The website switches between profile lengths of 3, 4, and 5
    if(len(content) == 3):
        profile = [
            content[2].get_text().replace(',', ' -'),
            content[1].get_text().replace(',', ' -'),
            content[0].get_text().replace(',', ' -'),
            base_url + link.get('href')
        ]
    if(len(content) == 4):
        profile = [
            content[3].get_text().replace(',', ' -'),
            content[2].get_text().replace(',', ' -'),
            content[1].get_text().replace(',', ' -'),
            base_url + link.get('href')
        ]
    if(len(content) == 5):
        profile = [
            content[4].get_text().replace(',', ' -'),
            content[3].get_text().replace(',', ' -'),
            content[2].get_text().replace(',', ' -'),
            base_url + link.get('href')
        ]

    profiles.append(profile)

with open('profiles.csv', 'w') as f:
    for profile in profiles:
        f.write(','.join(profile) + '\n')
