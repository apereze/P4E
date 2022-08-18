def computepay(h, r):
    if h <= 40:
        pay = h*r
    else:
        diffh = h - 40
        pay = (40*r)+(diffh*r*1.5)
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h, r)
print("Pay", p)
