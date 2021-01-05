from datetime import datetime
datestr = "NOV 02, 2016"
datetime_object = datetime.strptime(datestr, '%b %d, %Y')
print(datetime_object)
