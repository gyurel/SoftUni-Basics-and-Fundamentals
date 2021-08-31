company_info = {}

command = input()
while command != 'End':
    cmd_info = command.split(' -> ')
    company_name = cmd_info[0]
    employee_id = cmd_info[1]

    if company_name not in company_info.keys():
        company_info[company_name] = []

    if employee_id not in company_info[company_name]:
        company_info[company_name].append(employee_id)

    command = input()

for (company, employee_ids) in sorted(company_info.items(), key=lambda kvp: kvp[0]):
    print(company)

    for emp_id in employee_ids:
        print(f'-- {emp_id}')
