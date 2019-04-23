#to create and then delete a file
import os
f=open("mom.txt","w")
f.close()
os.remove("mom.txt")
