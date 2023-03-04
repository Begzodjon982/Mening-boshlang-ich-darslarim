yosh = int(input("yoshingiz nechida?"))
if yosh <= 4:
    narx = 0
elif yosh <= 12 :
    narx = 5000
else:
    narx = 10000

print(f"sizga kirish {narx}so'm")