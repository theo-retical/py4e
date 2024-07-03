def computepay(h, r):
    h = float(hrs)
    r = float(rate)
    pay = h * r
    ot_h = h - 40.0
    ot_r = r * 1.5
    ot_pay = ot_h * ot_r
    std_pay = 40 * r
    if h <= 40:
        return pay
    else:
        return std_pay + ot_pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(hrs, rate)
print("Pay", p)
