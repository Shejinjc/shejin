from datetime import date, timedelta
import csv
with open('dateee.csv','w') as outputfile:
    csv_writer = csv.writer(outputfile,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    d1 = date(2017, 10, 5)  # start date
    d2 = date(2017, 11, 5)  # end date
    delta = d2 - d1         # timedelta
    for i in range(delta.days + 1):
        csv_writer.writerow([d1 + timedelta(i)])
        print(d1 + timedelta(i))
