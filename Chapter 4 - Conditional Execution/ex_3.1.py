hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
h_ot = h - 40
r_ot = r * 1.5

if h <= 40:
    print(h * r)
else:
    pay_std = 40 * r
    pay_ot = h_ot * r_ot
    total_pay = pay_std + pay_ot
    print(total_pay)
