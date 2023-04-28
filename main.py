import requests
import pandas as pd
from bs4 import BeautifulSoup

import requests

# if you want to see the moving proxies:- wathch this video:- https://www.youtube.com/watch?v=mJi5VyaXDQQ

reviewlist = []

def extractReviews(producturl,head):
    resp = requests.get(producturl, headers=head)
    print(resp)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for i in soup.find_all('div',{'data-hook':"review"}):
        review = {
            'title' : soup.title.text.replace('Amazon.in:Customer reviews: ','').strip(),
            'review_body' : i.find('span',{'data-hook': 'review-body'}).text.strip(),
            'rating' : i.find('i', {'data-hook': 'review-star-rating'}).text.strip(),
            'review_title': i.find('a',{'data-hook':'review-title'}).text.strip()
        }
#         print(review.items())  
        reviewlist.append(review) 


def totalPages(head):
    url = 'https://www.amazon.in/ASUS-15-6-inch-NVIDIA-GeForce-RTX-3050-Battery-FA506ICB-HN005W/product-reviews/B09ZXVY6NR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
    resp = requests.get(url, headers=head)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.find('div', {'data-hook':"cr-filter-info-review-rating-count"})
    return int(reviews.text.strip().split(', ')[1].split(" ")[0])


def main():
#     pageNumber = 3
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0'
    }

    productUrl = 'https://www.amazon.in/ASUS-15-6-inch-NVIDIA-GeForce-RTX-3050-Battery-FA506ICB-HN005W/product-reviews/B09ZXVY6NR/ref=cm_cr_arp_d_paging_btm_3?ie=UTF8&pageNumber=1&reviewerType=all_reviews'

    
    totalPg = totalPages(HEADERS)
    print(totalPg)

    
    for i in range(1, totalPg//10+1):     
        print(f"Running for page {i}")
    
        try:
            reviewUrl = productUrl.replace('pageNumber=1', f'pageNumber={i}')
            print(reviewUrl) 
            extractReviews(reviewUrl, HEADERS)
        except Exception as e:
            print(e)
        
    df = pd.DataFrame(reviewlist)
    
    df.to_excel('output.xlsx', index=False)
    
main() 





# we can also use header:- 
#     HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#     'Accept-Language': 'en-US, en;q=0.5'
# }