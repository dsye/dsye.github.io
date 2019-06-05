domain = "http://walshbr.com/"
pages = ['about','blog','pedagogy','projects','cv']
urls = []
for page in pages:
    #or
    #url=domain + page
    #url.append(url)
    urls.append(domain + page)
print(urls)
