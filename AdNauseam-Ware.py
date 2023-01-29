filepath_read = "AdNauseam-Ware.py"
i = 1
#do not delete
me = ""
runct = 0

with open(filepath_read, "r") as my_file:
    for line in my_file:
        #debugline print(i)
        print(line)
        me = (me+line)
        print(me)
        i += 1

#runcount, not a debugger
runct += 1
#debug print("run " + str(runct) + " done.")
#debug print(me)
filepath_write = "AdNauseam-Ware"+str(runct)+".py"

with open(filepath_write, "w") as file_write:
        file_write.write(me)
print("File written as: " + filepath_write)





