#1 pyhton program to check leap year

#input from the user

year = int(input("enter a year:"))

#check if the year is a leap year or not 

if ( year % 4 == 0 and year % 100 != 0 or (year % 400 == 0)):
    print(f'{year} is leap year ')

else :
    print(f'{year} is not a leap year')
    
