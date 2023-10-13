from config import ACCESS_TOKEN, PAGE_ID, API_KEY
import requests
from bs4 import BeautifulSoup


def post_to_fb_page(msg, image_url):
    post_url = 'https://graph.facebook.com/v18.0/{}/photos'.format(PAGE_ID)
    payload = {
        'message': msg,
        'access_token': ACCESS_TOKEN,
        'url': image_url
    }

    # Uploading on FB Group
    r = requests.post(post_url, data=payload)
    data = r.json()
    print(data)
    if 'id' in data:
        return True
    else:
        return False


def get_featured_recipie():
    URL_TO_SCRAPE = 'https://allrecipes.com/'
    title = None
    image_url = None

    headers = {
        'authority': 'www.allrecipes.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ur;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'cache-control': 'no-cache',
        'dnt': '1',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    }
    payload = {'api_key': API_KEY, 'url': URL_TO_SCRAPE, 'render': 'true'}
    r = requests.get('http://api.scraperapi.com', params=payload, timeout=60)
    # r = requests.get(URL_TO_SCRAPE, headers=headers, timeout=30)

    html = r.text.strip()
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('#card--featured_1-0 .card__title-text')[0].text.strip()
    image_url = soup.select('#card--featured_1-0 img')[0]['data-src'].strip()
    return title, image_url
