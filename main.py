
ex="1"
while ex != "0":
    print("Exercice Nº (insert 0 to end)")
    ex=input()
    print(f"Exercise {ex} selected")
    if ex=="1":
        #Ex 1--------
        exec(open("Lab 2-1.py").read())
    elif ex=="2":
        # Ex 2-------
        exec(open("Lab 2-2.py").read())
    elif ex=="3":
        # Ex 3-------
        exec(open("Lab 2-3.py").read())
    elif ex=="4":
        # Ex 4-------
        exec(open("Lab 2-4.py").read())
    else:
        print(f"Exercise {ex} doesn't exiat")

