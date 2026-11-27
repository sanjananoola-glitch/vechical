
v = input("Enter vehicle type: ")
h = int(input("Enter parking hours: "))
n = input("Enter vehicle number: ")

if v == "two-wheeler":
    fee = h * 20
elif v == "four-wheeler":
    fee = h * 50
elif v == "heavy":
    fee = h * 100
else:
    fee = 0

print("Vehicle:", v)
print("Number:", n)
print("Hours:", h)
print("Parking fee:", fee)