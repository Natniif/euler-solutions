#first we need to define if the monday falls on the day from 1 jan 1900

def is_sunday(n): 
    if n== 7: 
        return True
    return False 

# Next need to define if it is the start of a mont

def is_start_of_month(n): 
    counter = 0
    year = n//365
    if n <  4: 
       from_start = n - year*365
        #january
       if from_start - 31 == 0:
           return True
       #february 
       elif from_start - (28+31) == 0:
           return True
       #march
       elif from_start - (28+62) == 0:
           return True 
       #april
       elif from_start - (28+92) == 0: 
           return True 
       #may
       elif from_start -  (28 + 92 + 31) == 0: 
           return True 
       #june 
       elif from_start - (28 + 123 + 30) == 0: 
           return True
       #july 
       elif from_start - (28 + 153 + 31) = 0:
           return True
       #August 
       elif from_start - (28 + 154 + 31) == 0: 
           return True
       #september 
       elif from_start - (28 + 185 + 31) == 0:
           return True
       #october 
       elif from_start - (28 + 216 + 31) == 0: 
           return True
       #November
       elif from_start - (28 + 247 + 30) == 0: 
           return True 
       elif from_start == 0 return True
    elif n > 4:
            




