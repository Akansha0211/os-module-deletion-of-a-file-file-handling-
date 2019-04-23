#to create and then delete a file
import os
f=open("mom.txt","w")
f.close()
os.remove("mom.txt")
#if fie exists then delete
if os.path.exists("ma.txt"):    # when executed second time then prints The file does not exist on the console screen
    os.remove("ma.txt")
else:
    print("The file does not exist")

