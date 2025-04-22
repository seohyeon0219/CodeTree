date = input()
new_date = date.split('-')
month = new_date[0]
day = new_date[1]
year = new_date[2]
print(f'{year}.{month}.{day}')