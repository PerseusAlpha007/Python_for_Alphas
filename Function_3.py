def student_result(students):
    total_percentage = 0
    for i in students:
        total = (sum(i["marks"]))
        percentage = round(total / len(i["marks"]) , 2)
        i["total"] = total
        i["percentage"] = percentage
        print(i)
        total_percentage += i["percentage"]
    return round(total_percentage/len(students), 2)

list_students = [{"name":"Ava","marks":[45,74,85,85,65,65]},
                 {"name":"Brian","marks":[55,35,64,92,54,85]},
                 {"name":"Cole","marks":[95,85,74,65,64,35]},
                 {"name":"David","marks":[57,84,82,63,61,45]},]
avg_percentage = student_result(list_students)
print("Average Percentage of all students i = ",avg_percentage)




        










