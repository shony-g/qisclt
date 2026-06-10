import re

with open('regex_practice_dataset.txt', 'r') as f:
    data = f.read()
    vandi = re.findall(r'\w{2}-\d{2}-\w{2}-\d{4}', data)
    print(vandi)

    # empid = re.findall(r'EMP\d{3}',data)
    # print(empid)

    # print()

    # emailid = re.findall(r'\w+.?\w+@\w+\.\w\w\w?',data)
    # print(emailid)

    print()

    panc = re.findall(r'[A-Z]{5}\d{4}[A-Z]',data)
    print(panc)