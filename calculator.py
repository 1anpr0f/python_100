num1 = int(input("enter number: "))
num2 = int(input("enter number: "))

print("chose calculation: \n",
      "add \n",
      "subtract \n",
      "divide \n",
      "multiply \n")

calc =input()

if calc.lower() == "add":
    ans = num1 + num2
elif calc.lower() == "subtract":
    ans = num1 - num2
elif calc.lower() == "divide":
    ans = num1 / num2
elif calc.lower() == "multiply":
    ans = num1 * num2
    
print (ans)  
