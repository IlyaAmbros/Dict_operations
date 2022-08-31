# money problem / 3 month
# HW1 : Calculate balance for 3 month

money = {
    'Jan' : {
        'salary': 1500 , 
        'espense': 500 ,
        # balance
    } ,
    'Feb' : {
        'salary': 1200 , 
        'espense': 1700 ,
    } ,
    'Mar' : {
        'salary': 1700 , 
        'espense': 700 ,
    } ,
}

month = [ 'Jan' , 'Feb' , 'Mar' ]
for i in range(len(month)) :
    balance = money[month[i]]['salary'] - money[month[i]]['espense']
    money[month[i]].update({"balance": balance})
    print(f"{i+1}) {money[month[i]]['salary']} - {money[month[i]]['espense']} = {money[month[i]]['balance']}")
