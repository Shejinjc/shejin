import datetime
import csv
with open('ts&ccex.csv','w') as outputfile:
  with open('ts&cc1.csv','r') as input_file:
    csv_reader = csv.reader(input_file,delimiter=',')
    csv_writer = csv.writer(outputfile,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    line_count = 0
    for row in csv_reader:
      if(line_count == 0):
        csv_writer.writerow(['date','year','month','dayofyear','dayOfMonth','dayOfWeek','week','maxtemp','mdsetotal','numcust'])
        line_count+=1
      else:
        date = row[0]
        date_array=date.split('/')
        year_date=date_array[2]
        month_date=date_array[0]
        day_date=date_array[1]
        temp_date = datetime.datetime(int(year_date),int(month_date),int(day_date))
        weekday = temp_date.strftime("%w")
        dayofyear = temp_date.strftime("%j")
        weekyear = temp_date.strftime("%U")
        csv_writer.writerow([date,year_date,month_date,day_date,dayofyear,weekday,weekyear,row[1],row[2]])
        line_count +=1
