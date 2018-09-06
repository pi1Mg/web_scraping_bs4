from bs4 import BeautifulSoup
import requests
import csv


headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
source = requests.get('http://coreyms.com', headers=headers).text

soup = BeautifulSoup(source, "lxml")

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])


for article in soup.find_all('article'):
    # print(article.prettify())

    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    vid_src = article.find('iframe', class_='youtube-player')['src']
    print(vid_src)

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    # print(vid_id)

    yt_link = 'https://youtube.com/watch?v={}'.format(vid_id)
    print(yt_link)

    # print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()

# If something is missing, we can use try: except:
