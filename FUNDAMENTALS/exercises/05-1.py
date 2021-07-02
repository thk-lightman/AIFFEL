EmployeeID = [
    "OB94382",
    "OW34723",
    "OB32308",
    "OB83461",
    "OB74830",
    "OW37402",
    "OW11235",
    "OB82345",
]

Production_Employee = [P for P in EmployeeID if P.startswith("OB")]
print(Production_Employee)
