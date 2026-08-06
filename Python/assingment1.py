plant = input("enter your plant name ")
if plant == "rose":
    print("water the plant every day" )
    p1 = input("enter the colour you want for palnt")
    if p1 == "yellow":
        print("nice choice!!")
        p1_2 = input("enter the plant name")
        if p1_2 == "cactus":
             print ("water the plant twice a week")
             p2 = input("enter the location where you want to plant")
             if p2 =="amazon jungle":
                  print ("plant will not servive")
                  if p2 =="desert":
                       print ("excillent location for plant")
                  else :
                       print("this location is not good for your plant")
             else:
                print("try for desert land to palnt cactus")
        else:
            print("try new tree to plant")
    else:
        print("try new tree to palnt")  
else:
    print ("information of this plant not existed")