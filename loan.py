
money_owed = float(input('How much money do you owe, in dollars?\n'))
apr = float(input('What is the annual percentage?\n'))
payment = float(input('What will your monthly payment be, in dollars?\n'))
months = float(input('How many months do you want to see the results for?\n'))

monthly_rate = apr/100/12

for i in range(months):
  intrest_paid = money_owed * monthly_rate
  money_owed = money_owed + intrest_paid

  if (money_owed - payment < 0):
    print('They last payment is', money_owed)
    print('You paid off the loan in', i+1, 'months')
    break

  money_owed = money_owed - payment

  print('paid', payment, 'of which', intrest_paid, 'was interest.')
  print('Now I owe', money_owed)



