#The price of a child's meal (floating point)
#The price of an adult's meal (floating point)
#The number of children (integer)
#The number of adults (integer)
#The sales tax rate (floating point)
#Then, complete the following steps:
#Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by 
#the price of their meal, and multiplying the number of adults by the price of their meal and 
#adding those two values together.
#Display the subtotal.
#Ask the user for the the payment amount (floating point)
#Compute and display the change.

print('PAYMENT RECIEPT')
child_meal= input("please enter child's meal price: $")
adult_meal= input("please enter adult's meal price: $")
num_child= input("please enter number of children: ")
num_adult= input("please enter the number of adults: ")
sales_tax_rate= input("please enter tax rate: ")
sub_total= ((float(child_meal) * int(num_child)) + (float(adult_meal) * int (num_adult)))
sales_tax= (float(sales_tax_rate) / 100)
total= (sub_total + sales_tax)
print(f'Subtotal: ${sub_total:.2f}')
print(f'Sales tax: ${sales_tax}')
print(f'Total: ${total:.2f}')
user_payment= input('please enter payment amount: $')
change= (float(user_payment) - float(total))
print(f'change: ${change:.2f}')
print('Thank you for patronizing Foodie resturant')