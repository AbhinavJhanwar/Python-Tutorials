
import time

def calctime(f):
    def wrap(*arg,** kwargs):  #a=10,b=20
        print(arg)
        start=time.time()
        result=f(*arg,** kwargs)
        end=time.time()
        print(f.__name__+" took "+ str((end-start)*1000))
        print(result)
    return wrap

    

@calctime
def calcsum(a,b):
    
    result =a+b
    #print(result)
    return result
    
    
@calctime
def calcsub(a,b):
    
    result= a-b
    #print(result)
    return result
    

    
calcsum(10,20)
calcsub(10,20) 
