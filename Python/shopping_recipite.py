n = int(input("how many product: "))
subtotal= 0
for i in range (n):
    print("\n product",i+1)
    name= input("enter product name: ")
    price = float(input("enter product price: "))
    quantity = int(input("enter the quantity: "))
    

    amount= price * quantity 

    subtotal = amount + subtotal

    print("amount= $", amount)

match subtotal :
    case x if x >=10000:
        discount_percentage= 20

    case x if x >=7000:
        discount_percentage= 15
    case x if x>= 5000:
        discount_percentage= 10
    case x if x>=2000:
        discount_percentage= 5
    case _:
        discount_percentage= 0
discount = subtotal * discount_percentage/100
after_discount = subtotal - discount


gst = after_discount * 18/100

final_total= after_discount+ gst

print("\n Payment method")
print("\n1.Cash")
print("\n2.Upi")
print("\n3.card")

choice =int(input("choose the payment method"))
match choice:
    case 1 :
        payment_method="Cash"
    case 2 :
        payment_method="Upi"
    case 3 :
        payment_method="Card"
    case _ :
        payment_method="Unknown"

amount_paid = float(input("enter the amount paid"))
change = amount_paid - final_total 


print ("subtotal          :$",subtotal)
print ("discount          :",discount_percentage,"%")
print ("discount          :$",discount)
print (" After discount   :$",after_discount)
print ("Final total       :$",final_total)
print ("Payment method    :$",payment_method)
print ("amount paid       :$",gst)

if change >=0:
    print("change         :$",change)
else :
    print("amount due     :$",abs(change))

    