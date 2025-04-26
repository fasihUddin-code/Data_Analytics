import string

#Question_1
txt = "hello python world"
result = txt.replace(" ","_")
#print(result)
result2 = result.split("_")
#print(result2)
result3= "-".join(result2)
#print(result3)

#Question_2
word = "Javascript"
#print(len(word)>5)

#Question_3
num2 = 12
#print((num2 % 2==0) and num2 > 10)

#Question_4
num3 = 3
#print((num3<5) or (num3 > 20))

#Question_5
'''age = 25
has_id = True
if(age > 18 and age < 65):
    print("Valid ID")
else:
    print("Invalid ID")  '''  

#Question_6    
'''url = "http://www.facebook.com"
if (url.startswith("https://") or url.startswith("http://")):
    print("Valid URL")
else:
    print("Invalid URL")'''

#Question_7
itm_price = 100
itm_price -= (10/100)
#print("After Discount Item Price:",itm_price)

#Question_8
'''premium_customers = ["alice@example.com","charlie@example.com","bob@example.com"]
basic_customers = ["alex@example.com","divid@example.com","chloe@example.com"]
userEmail = "alice@example.com"
if ( userEmail in premium_customers) and (userEmail in basic_customers):
    print("userEmail exist in both types of customers")
else:
     print("userEmail does not exist in both types of customers")'''

#Question_9
'''def check_password(password):
    ls_upperChar = any(char.isupper() for char in password)
    ls_lowerChar = any(char.islower() for char in password)
    ls_space = ' ' in password
    print(password)
    print("space agaya",ls_space)
    ls_spcChar = any(char not in string.ascii_letters + string.digits + ' ' for char in password)

    if (ls_upperChar and ls_lowerChar and not ls_space and ls_spcChar):
        return True
    else:
        return False    

UserInput = input("Enter your password:")

result = check_password(UserInput)
print("Password is valid",result)'''

#Question_10
productCode = 'SKU-12345-XYZ'
print("first position of '-':",productCode.find('-'))
print("Number of dashes :",productCode.count('-'))
numericPart = productCode.removeprefix("SKU-").removesuffix("-XYZ")
print(numericPart)