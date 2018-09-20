# import requests
# import multiprocessing

# BASE_URI = 'http://elastic.pushshift.io/rs/submissions/_search/?q='

# def internet_resource_getter(stuff_to_get):
# #   session = session.Session()
#   stuff_got = []
  
#   for thing in stuff_to_get:
#     print(BASE_URI + thing)
#     response = requests.get(BASE_URI + thing)
#     stuff_got.append(response.json())

#   return stuff_got
  
# stuff_that_needs_getting = ['crypto', 'scam', 'ico']

# pool = multiprocessing.Pool(processes=3)
# pool_outputs = pool.map(internet_resource_getter,
#                         stuff_that_needs_getting)
# pool.close()
# pool.join()
# print (pool_outputs)

# #print Hello World!\n"


import grequests

def exception_handler(request, exception):
  print ("Request failed")

urls = [
    'http://www.heroku.com',
    'http://python-tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://fakedomain/',
    'http://kennethreitz.com'
]

rs = (grequests.get(u) for u in urls)
print(grequests.map(rs,exception_handler=exception_handler))
response = grequests.map(rs,exception_handler=exception_handler)
for res in response:
  print(res)