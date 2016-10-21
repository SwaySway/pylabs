import urllib.request
from operator import itemgetter
from datetime import datetime

url = 'http://chart.yahoo.com/table.csv?s=TGT'
page = urllib.request.urlopen(url)
page = [x.strip() for x in page.readlines()]
page = [str(x) for x in page]
page = [y.strip('b\' ') for y in page]
page.pop(0)
starting_date = [i for i, s in enumerate(page) if '2016-10-14' in s][0]
ending_date = [i for i, s in enumerate(page) if '2016-10-10' in s][0]
list_size = ending_date - starting_date
dates = [None] * list_size
high_shares = [None] * list_size
low_shares = [None] * list_size
close = [None] * list_size
volume = [None] * list_size

for x in range(list_size):
    dates[x] = page[x+starting_date].split(",")[0]
    high_shares[x] = float(page[x+starting_date].split(",")[2])
    low_shares[x] = float(page[x+starting_date].split(",")[3])
    close[x] = float(page[x+starting_date].split(",")[4])
    volume[x] = float(page[x+starting_date].split(",")[5])


lows_index = min(enumerate(low_shares), key=itemgetter(1))[0]
highs_index = max(enumerate(high_shares), key=itemgetter(1))[0]
highv_index = max(enumerate(volume), key=itemgetter(1))[0]
average_close = sum(close)/len(close)

low_day = dates[lows_index]
high_day = dates[highs_index]
highv_day = dates[highv_index]
style = "%Y-%m-%d"
low_day = datetime.strptime(low_day, style)
high_day = datetime.strptime(high_day, style)
highv_day = datetime.strptime(highv_day, style)

print(high_day.strftime("%A")+",", "share price is", "$"+str(high_shares[highs_index]), "the highest of the week.")
print(low_day.strftime("%A")+",", "share price is", "$"+str(low_shares[lows_index]), "the lowest of the week.")
print("Highest trading volume is", '${:,.2f}'.format(volume[highv_index]), "shares", "happened on "+highv_day.strftime("%A")+",")
print("Last weeks average closing price is", '${:,.2f}'.format(average_close))
