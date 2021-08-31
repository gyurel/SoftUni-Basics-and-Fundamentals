input_str = input()

company_employees = {}

while not input_str == "End":

    company_name_user_id = input_str.split(" -> ")

    company_name = company_name_user_id[0]
    user_id = company_name_user_id[1]

    if company_name not in company_employees:
        company_employees[company_name] = [user_id]
    else:
        if user_id in company_employees[company_name]:
            input_str = input()
            continue
        else:
            company_employees[company_name].append(user_id)

    input_str = input()

for key_company_name, val_user_id in sorted(company_employees.items(), key= lambda kvp: (kvp[0])):
    print(f"{key_company_name}")
    for id in val_user_id:
        print(f"-- {id}")
