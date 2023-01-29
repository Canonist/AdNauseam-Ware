filepath_read = "v2AdNauseam-Ware.py"
me = ""
runct = 0

with open(filepath_read, "r") as my_file:
     for line in my_file:
        #debugline print(i)
        print(line)
        me = (me+line)
        print(me)

#write copy as file#.py
while True:
    print(runct)
    runct += 1
    filepath_write = "v2AdNauseam-Ware" + str(runct) + ".py"
    with open(filepath_write, "w") as file_write:
            file_write.write(me)





