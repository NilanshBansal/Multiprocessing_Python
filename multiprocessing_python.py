import requests
from multiprocessing.dummy import Pool

url = 'http://elastic.pushshift.io/rs/submissions/_search/?q='


def req_split(r):
    # requests.head is much faster than requests.get if your intention is only to get the status code
    req = requests.head(url+ r)
    print(req.status_code)
    if req.status_code == 200:
        # print(url + r)
        temp = r  # return the url string if the server report OK
    else:
        temp = 0
    return temp


data = ['crypto', 'scam', 'ico','litecoin']

with Pool(10) as p:
    pm = p.imap_unordered(req_split, data)
    pm = [i for i in pm if i]
    print(pm)
