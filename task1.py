from utils.csvhandle import Employee

def task1():
    new = {}
    for emp in Employee.readcsvdetail():
        if int(emp["SALARY"]) > 9000:
            fn, ln, ph, sal, em = emp['FIRST_NAME'], emp['LAST_NAME'], emp['PHONE_NUMBER'], emp['SALARY'], emp['EMAIL']
            new.update({"Name": f"{fn} {ln}"})
            new.update({"Email": em})
            new.update({"Phone": ph.replace('.', '')})
            new.update({"Salary": sal})
            print(new)