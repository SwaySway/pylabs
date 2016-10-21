import urllib.request

url = 'http://chart.yahoo.com/table.csv?s=TGT'
page = urllib.request.urlopen(url)
page = [x.strip() for x in page.readlines()[4:9]]
page = [str(x) for x in page]
page = [y.strip('b\' ') for y in page]
print(page[2].split(","))