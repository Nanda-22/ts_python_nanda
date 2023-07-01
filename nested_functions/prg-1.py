#nested functions
def f1():
    print("i am in f1")
    def f2():
        print("I am in F2")
        def f3():
            print("I am in F3")
        f3()
    f2()

f1()
