import csv
from csv import DictReader
from typing import Dict

class Employee:
    file = "/home/cyra/PycharmProjects/HRconnect/employees.csv"
    # absolute path of the csv file
    @classmethod
    def readcsv(cls) -> csv.DictReader:
        emp_details = {}
        with open(cls.file, "r") as f:
            dictr = DictReader(f)  # Converting file object into DictReader object
            for i in dictr:
                emp_details.update(i)
        return emp_details

    @classmethod
    def readcsvdetail(cls) -> Dict:
        with open(cls.file) as f1:
            for row in DictReader(f1):
                yield row