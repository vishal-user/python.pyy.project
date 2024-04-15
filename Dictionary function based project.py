company=["exploit","chip","neamat"]
passwords={"neamet":0000,"exploitchip":1111,"jan Mohammad":2222}
print(company[0],company[1]) 
password=int(input("Enter your pin"))

def find_in_file(f):
    myfile=open("names.txt")
    Names=myfile.read()
    Names=Names.splitlines()
    if f in Names:
        return "That name is in the database"
    else:
         return "That Name is not in the database!"

if password in passwords.values():
     name=input("enter name:")
     print(find_in_file)
else:
     print("incorrect password")
     print("This info can be accesed only by:")
     for key in passwords.keys():
          print(key)

    

    
                
          