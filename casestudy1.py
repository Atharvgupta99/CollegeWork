a=float(input("$"))
b=float(input("$"))
c=float(input("$"))
d=a+b+c
if (d>50):
  dp=d-(0.1*d)
  print(f"{dp}$")
else:
  print(f"${d}")