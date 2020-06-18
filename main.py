y = int(input("Enter a year: "))  
if (y % 4) == 0:  
   if (y % 100) == 0:  
       if (y % 400) == 0:  
           n = 366 
       else:  
           n = 365
   else:  
       n = 366
else:  
   n = 365
   
b = 2005
c = 58000.0

m = str(input("Enter a month: "))
if m == "January":
    m = 0
    if n == 366:
        m = 1
        
if m == "February":
    m = 31
    if n == 366:
        m = 32
        
if m == "March":
    m = 59
    if n == 366:
        m = 60
        
if m == "April":
    m = 90
    if n == 366:
        m = 91
        
if m == "May":
    m = 120
    if n == 366:
        m = 121
        
if m == "June":
    m = 151
    if n == 366:
        m = 152
        
if m == "July":
    m = 181
    if n == 366:
        m = 182
        
if m == "August":
    m = 212
    if n == 366:
        m = 213
        
if m == "September":
    m = 243
    if n == 366:
        m = 244
        
if m == "October":
    m = 273
    if n == 366:
        m = 274
        
if m == "November":
    m = 304
    if n == 366:
        m = 305
        
if m == "December":
    m = 334
    if n == 366:
        m = 335

        
d = int(input("What's the day of the month?: "))
Stardate = float(c + (1000*(y-b)) + ((1000/n)*(m + d -1)))
print ("%0.02f" % Stardate)