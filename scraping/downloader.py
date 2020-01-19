import os

with open('all_paper_links.txt', 'r') as file:
    links = file.read().splitlines()

i = 1
year = 0
issue = 0
for link in links:
    if year != link[50:54]:
        year = link[50:54]
        i = 1
    issue = link[61:63]

    os.system(f'curl -o ./data/{year}_{issue}_{i}.pdf {link}')

    i += 1