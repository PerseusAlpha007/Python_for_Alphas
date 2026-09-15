'''
Positional Argument
in this kind of argument we can not change the positions of paramerters in the
argument parenthesis
'''
# def result(seat_no,name,marks):
#     print("Seat_no. = ",seat_no)
#     print("Name = ",name)
#     print("Percentage = ",sum(marks)/len(marks))


# result("Ashmir",54218721,[54,65,98,78,58])
# print(result)

'''
Keyworded Argument
in this type of argument we can change the positions of argument but
we have to specify in function cal both the variable and the corrosponding 
value
'''

# def result(seat_no,name,marks):
#     print("Seat_no. = ",seat_no)
#     print("Name = ",name)
#     print("Percentage = ",sum(marks)/len(marks))


# result(name = "Ashmir",seat_no = 54218721,marks = [54,65,98,78,58])
# print(result)
'''
Arbitariry Argument
In this kind of argument we can pass multiple arguments in one variable 
in the for of tuple using "*" before the variable in the function definition
NOTE = The Arbitariry argument must always be at the end of parameter parenthesis
'''

# def display_student_data(name,*marks):
#     print("Name = ",name )
#     print("Marks = ",*marks)


# display_student_data("Sandy",45,32,89,97,45,)
# display_student_data("Tina",78,65,9,68,75)

'''
Keyworded Arbitariry Argument
In this argument we can pass multiple keyworded arguments in a single argument 
in the form of a dictionary by using "**"
NOTE = The Keyworded Arbitariry argument must always be at the end of parameter parenthesis
'''
def display_location(Country,state,**C):
    print("Country_Name = ",Country)
    print("State = ",state)
    print("Coordinates = ",C)

display_location("India" , "Maharashtra" ,Longitude = 74.53 , Latitude = 20.56 ,city = "Malegaon")
