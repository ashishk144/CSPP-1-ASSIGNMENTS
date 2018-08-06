def paying_debtoffinayear(bal_ance, annual_interestrate):
    """defining paying function"""
    ba_l = bal_ance
    epsi_lon = 0.05
    low_pay = ba_l/12
    high_pay = (ba_l * (1 + (annual_interestrate/12))**12)/12.0
    pa_y = (high_pay + low_pay)/2
    while True:
        i = 12
        ba_l = bal_ance
        while i != 0:
            u_bal = ba_l - pa_y
            ba_l = u_bal + ((annual_interestrate / 12.0) * u_bal)
            i -= 1
        if ba_l > epsi_lon:
            low_pay = pa_y
        elif ba_l < -epsi_lon:
            high_pay = pa_y
        else:
            return round(pa_y, 2)
        pa_y = (high_pay + low_pay)/2
def main():
    """defining main"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " +str(paying_debtoffinayear(data[0], data[1])))
if __name__ == "__main__":
    main()
