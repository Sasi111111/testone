#decorators in python
#decorators are used to extend  the behavior of the existing function without modifying it
# in python we can pass a function as a argument and we can return a function also
 
def fun():
    print("my name is luffy")
#this is normal function and now we are going to extend its behaviour with out modifying it by using decorator
def fun1(fun):
    def inner():
        print("iam going to become the king of pirates")
        fun()
    return inner
x=fun1(fun)
x()
#python provides a simple way to use the decorators
@fun1
def fun2():
    print("iam son goku")
#fun2()

