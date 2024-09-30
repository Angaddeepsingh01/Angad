



# f = open("angad.txt")

# line = f.readline()


# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close



# a = "itt"

# f =open("angad.txt","a")     

# f.write(a)

# f.close



# with open("angad.txt") as f :       # with 'with' fuction you don't have to close the file 

    # print(f.read())               




# with (open("ps.txt")) as a :
    
#     if( "twinkle" in a.read() ):
#         print("yes")
#     else:
#         print("no")


# import random

# def game():
#     print("you are playing the game ....")
#     score = random.randint(1,65)
    

#     with open("game.txt") as a :
#       hiscore = a.read()

#       if(hiscore !=""):
#          hiscore = int(hiscore)

#       else:
#           hiscore = 0

#     print(f"your score is {score}")

#     if(score>hiscore):
#         with open("game.txt", "w") as a:

#             a.write(str(score))


#     return score

# game()







# def gen_table(n):
#     table  = ""
#     for i in range (1 , 11):
#         table += f"{n} * {i} = {n*i}\n"

#         with open(f"tables/table{n}.txt" , "w")as a :
#             a.write(table)
            

# for i in range (2,21):
#   gen_table(i)
    



# with open("donkeyfile.txt", "r") as a :
#      content  = a.read()
# contentnew = content.replace( "donkey" , "######")


# with open ("donkeyfile.txt", "w")as a :
#      a.write(contentnew)





# with open ("log.txt") as a :
#     lines = a.readlines()

# lineno = 1

# for line in lines:
#      if("python" in line ):
        
#         print(f"yes line no is {lineno}" )
#         break
#      lineno+=1
     
# else:
#         print("no")



# to make a copy of file : following should be done 

# with open("this.txt") as f:
#     content = f.read()
# with open("this_copy.txt", "w")as f :
#     f.write(content)






# with open("this.txt") as f:
#     content = f.read()


# with open("this_copy.txt")as f :
#     content2 = f.read()


# if(content == content2):
#     print("yes the data in file is same")

# else:
#     print("no the data in file is not same")



# TO WIPE OUT THE DATA IN FILE :

# with open("this_copy.txt" , "w")as f :
#     f.write("")             




# to rename a file following should be done 


import os

with open("forrename.txt") as f :
    content = f.read()
os.remove("forrename.txt")

with open("renamed.txt" , "w") as f :
    f.write(content)