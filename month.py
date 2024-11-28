import calendar
 
 
year = 2025
 
print ("select month: ")

clas = input()
month = int(clas)

x = calendar.month(year,month)
print(x)