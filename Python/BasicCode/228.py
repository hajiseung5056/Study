def calc_monthly_salary(num):
    result = str(num/12)
    result_list = result.split(".")
    print(result_list[0])

calc_monthly_salary(12000000)


#def calc_monthly_salary(annual_pay) :
#    monthly_pay = int(annual_pay / 12)
#    return monthly_pay
# int() 사용하여 형변환 시 소수점은 버림 처리