is_male = False
is_tall = True

if is_male or is_tall: 
    print("you are a tall female")
else:
    print("You are a female")

if is_male and is_tall:      #difference between OR and AND -> if Male is true and tall is true
    print("you are a tall female")  
else:
    print("You are a female")


if is_male and is_tall:     
    print("you are a tall female")  
elif is_male and not(is_tall):
    print("You are a female")
else:
     print("You are a ???")