import csv,requests,os
from bs4 import BeautifulSoup

HN_URL='https://news.ycombinator.com/'
CSV_FILE='hn_top20.csv'

def fetch_top_post():
    try:
        response = requests.get(HN_URL,timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Network error \n {e}')
        return []
        
        
    soup = BeautifulSoup(response.text,'html.parser')
    post_links = soup.select('span.titleline > a')
    
    posts = []
    
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get('href').strip()
        
        posts.append({"title":title,"URL":url})
        
    return posts

def save_to_csv(posts):
    if not posts:
        print('Nothing to save')
        return
    
    with open(CSV_FILE,'w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f,fieldnames=['Title','URL'])
        writer.writeheader()
        for post in posts:
            writer.writerow({'Title':post['title'],'URL':post['URL']})
        
    print(f'Saved {len(posts)} posts to {CSV_FILE}')
        
def main():
    print('Fetching top posts from Hacker News...')
    top_posts = fetch_top_post()
    
    if top_posts:
        print(f'Fetched {len(top_posts)} posts. Saving to CSV...')
        save_to_csv(top_posts)
    else:
        print('No posts fetched.')
        
if __name__ == '__main__':
    main()