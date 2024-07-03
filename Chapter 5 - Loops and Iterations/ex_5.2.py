largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        numcheck = int(num)
        if largest == None:
            largest = numcheck
        elif largest < numcheck:
            largest = numcheck
        if smallest == None:
            smallest = numcheck
        elif smallest > numcheck:
            smallest = numcheck
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
