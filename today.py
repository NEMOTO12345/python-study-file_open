import datetime

i = open('today.txt','w')
i.write(str(datetime.date.today()))
i.close()