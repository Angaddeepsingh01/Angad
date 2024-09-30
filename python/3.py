from datetime import datetime

def calc():

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    names = {"angad": 1.80 , "sahil" :1 , "rohan" : 2}
    name = list(names.keys())
    print(name)
    user = input("enter the name : ").lower()

    if(user in names):
        u = names.get(user)
        print(f"the amount he takes is {u}")
        weight = float(input("enter the weight : "))
        purity = float(input("enter the purity : "))
        l = u
        combo = purity + l 
        
        pure = weight*combo
        pure = round(pure/100,3)

        finale = f"{weight} * {purity} + {u} = {round(combo, 2)}\n Final pure value: {pure}\n"

        print(finale)
        with open(f"{user}.txt" , "w")as f :
            f.write(f"{current_time}\ncalculation for {user} \n {finale} ")
    else:
        print("something went wrong")
        

calc()





