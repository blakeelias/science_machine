from bs4 import BeautifulSoup
import requests

def get_page(link):
    page_request = requests.get(link)
    page = BeautifulSoup(page_request.content, 'html.parser')
    return page

def get_all_links(page, pattern):
    all_links = []

    for item in page.find_all('a'):
        raw_link = item.get('href')
        if raw_link.startswith(pattern):
            clean_link = raw_link.split(';',1)[0]
            all_links.append(clean_link)
            # print(clean_link)

    return(all_links)

# def get_all_papers(issue_links):
#     paper_links = []
#     for issue in issue_links:
#         issue_page = get_page()
#         get_all_links(issue_page, pattern='/contentone/imp/jcs/')

home_link = 'https://www.ingentaconnect.com/content/imp/jcs'
home_page = get_page(home_link)
issue_links = get_all_links(home_page, '/content/imp/jcs/')

all_paper_links = []
for issue in issue_links:
    page = get_page('https://www.ingentaconnect.com' + issue)
    paper_links = get_all_links(page, '/contentone/imp/jcs/')
    all_paper_links.extend(paper_links)

for link in all_paper_links:
    print(link)
        





    