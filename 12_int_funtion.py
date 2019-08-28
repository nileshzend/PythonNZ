# --------------------
# number_one = input("enter first number ")
# number_two = input("enter second number ")
# total = number_one + number_two
# print("total is " + total)
# total = "4" + "4" = 44
# ------------------------
number_one = int(input("enter first number "))
number_two = int(input("enter second number "))
total = number_one + number_two
# print("total is " + total)  # it will give your error
print("total is " + str(total))
# total = "4" "4" = 8

# str   (string function)
# 4 ---> "4"  it covert int to string

# int (integer function)
# "4" ---> 4     it convert string to int function

# float  (floting function)
# "4"  ---> 4.0

number1 = str(4)
number2 = float("44")
number3 = int("33")
print(number2 + number3)  #  we can add float and int but gives result in float
