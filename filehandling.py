# f=open("demofile.txt.txt","r")
# print(f.read())
# print(f.read(5))read only specific parts of file
# for x in f:
#     print(x)
# print(f.readline())


# f=open("demofile2.txt.txt","a")
# f.write("Now the file has more content!")
# f.close()


# f=open("demofile3.txt.txt","w")
# f.write("woops!the file has limited content!")
# f.close()

# import os
# os.remove("demofile3.txt.txt")

#check wheather the file exist or not

import os
os.path.exists("demofile2.txt.txt")