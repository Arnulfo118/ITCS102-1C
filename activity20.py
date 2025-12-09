isDirty = True

while isDirty == True:
    washing = input("Continue washing cloths?: (yes/no)").lower()

    if washing == "yes":
        print("Washing clothes now....")
        continue
    else:
        print("Stopped washing clothes.")
        break    
