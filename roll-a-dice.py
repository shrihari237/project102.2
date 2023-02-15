import random

response ="y"

en =input("Enter y to continue or n to exit")

while en =='y':
    no = random.randint(1,6)
    if response == 'n':
        break

    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
     
    elif no ==2:
        print("[-----]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[-----]")
       

    elif no ==3:
         print("[-----]")
         print("[     ]")
         print("[0 0 0]")
         print("[     ]")
         print("[-----]")

    elif no ==4:           
         print("[-----]")
         print("[0   0]")
         print("[     ]")
         print("[0   0]")
         print("[-----]")
        
    elif no ==5:
          print("[-----]")
          print("[0   0]")
          print("[  0  ]")
          print("[0   0]")
          print("[-----]")
        

    elif no ==6:
        print("[------]")
        print("[ 0  0 ]")
        print("[ 0  0 ]")
        print("[ 0  0 ]")
        print("[------]")


    en =input("Enter y to continue or n to exit")                      
           