largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done":
        break

    try:
        fnum = int(num)
    except:
        fnum = -999
    if fnum == -999:
        print('Invalid input')
        continue
    if largest is None:
        largest = fnum
    elif largest < fnum:
        largest = fnum

    if smallest is None:
        smallest = fnum
    elif smallest > fnum:
        smallest = fnum

print("Maximum is", largest)
print("Minimum is", smallest)
