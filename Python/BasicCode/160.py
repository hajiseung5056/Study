list = ["intra.h","intra.c","define.h","run.py"]

for val in list:
    val1 = val.split(".")
    if val1[1] == "h" or val1[1] == "c":
        print(val)