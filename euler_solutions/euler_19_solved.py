from datetime import date 

sundays = 0 

for year in range(1901,2001):
    for month in range(1,13):
        # date uses yyyy/mm/d format 
        # .weekday classifies what day of the week it is starting from monday == 0
        # Therefore the if statement is asking if a sunday is at the start of a month
        if date(year, month, 1).weekday() == 6:
            sundays += 1

print(sundays)
