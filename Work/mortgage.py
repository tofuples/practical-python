# mortgage.py
#
# Exercise 1.7

total = 500000.0
anual_rate = 0.05
montly_rate = anual_rate/12
payment = 2684.11
total_paid = 0.0
total_months = 0

extra_payment = 1000
extra_payment_startmonth = 61
extra_payment_endmonth = 108

while total > 0: #loop continua até o total a ser pago zerar
    total_months = total_months + 1 
    interest = total * (montly_rate) 
    total = total + interest     #atualiza o total a ser pago
      
    #Applying extra payment 
    if total_months >= extra_payment_startmonth and total_months <= extra_payment_endmonth: 
        total = total - extra_payment   #desconta o pagamento extra do total a ser pago
        total_paid = total_paid + extra_payment #adiciona o pagamento extra no valor pago 
     
     #Check if the remaing principal is less than regular payment    
    if total < payment: #se o total a ser pago for menor que o payment     
        payment = total
        
    total = total - payment
    total_paid = total_paid + payment   #atualiza o quanto já foi pago a cada mês
           
    print(total_months, round(total_paid, 2), round(total, 2))  
    
    
#print('Total paid:', round(total_paid, 2))
#print('Total Months:', total_months)

print(f'The total paid is ${round(total_paid,2)} and the total months is {total_months}')