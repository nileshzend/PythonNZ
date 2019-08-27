# print("2+3")  dont use ""
print(2+3)       # ANS : 5
print(2+3*4)     # ANS : 14  
print(2+3*4-1)   # ANS : 13 
print(4/2)       # ANS : 2.0  # floting print devision
print(2/4)       # ANS : 0.5
print(4//2)      # ANS : 2    # integre division
print(2//4)      # ANS : 0
print(2**3)      # ANS : 8    # double multiply means double power   
print(2**0.5)    # ANS : 1.4142135623730951

# Using round function
print(round(2**0.5,4))  # ANS : 1.4142   # 2 power 0.5 times & round or see 4 chracter
print(round(2**3.4,3))  # ANS : 10.556    # 2 power 3 times & round or see 3 chracter
# Precedence rule 
# OPERATORS	             PRECEDENCE AND ASSOCIATIVITY RULE
# PARENTHESE (Bracket)	 HIGHEST
# EXPONENT	             RIGHT TO LEFT
# * , / , //, %          LEFT TO RIGHT
# +, -	                 LEFT TO RIGHT
 # % means modulo
print(2**3/2*6-4*(3-4/2))  # ANS: 20.0   # in this case it will firstly calulate
                                         # inside the bracket then it will go left to right
# 1st (3-4/2)
# 2nd  2**3 = 8
# 3rd  8/2 = 4
# 4th  4*6 = 24
# 5th  24-4 = 20
# 6th 20*1.0 = 20.0  

print(3%2)     # ANS : 1  # % modulo give remiander 
print(3-1*2)   # ANS : 1
print((3-1)*2) # ANS : 4
print((2+3)*2)  # ANS : 10
print((2+3)/2)  # ANS : 2.5
# 2+3 = 5/2
print((2+3)*5/2%6) # ANS : 0.5
# 5 * 5 / 2 % 6
# 25 /2 % 6
# 12.5 % 6 
print(12.5 % 6)    # ANS : 0.5
# exponenets (**) double star means exponents
print(2**3**2)   #ANS : 512
# (2**9)
print(2**9)