print("GCD Finder")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
i = 1
gcd = 0
while i <= a and i <= b:
if a % i == 0 and b % i == 0:
gcd = i
i = i + 1
print("GCD:", gcd)
if gcd > 1:

print("Numbers are not co-prime")
else
print("Co-prime numbers")
lcm = (a * b) / gcd
print("LCM:", lcm