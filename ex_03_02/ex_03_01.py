hrs = input("Enter Hours:")
h = float(hrs)
rate = 10.5
pay = 0
if h <= 40:
    pay = h*rate
else:
    diffh = h - 40
    pay = (40*rate)+(diffh*rate*1.5)
print(pay)
