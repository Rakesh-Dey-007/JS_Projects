Rent = int(input("Enter total home rent : "))
Electricity = int(input("Enter total electricity bill : "))
Unit = int(input("Enter electricity unit : "))
Food = int(input("Enter total food bill : "))
Member = int(input("Enter room members : "))

Total_Electricity = Electricity * Unit
Total_Cost = Rent + Total_Electricity + Food
Rent_Per_Member = Total_Cost / Member

print(f"Each Room Member have to pay Rs. {Rent_Per_Member}")

