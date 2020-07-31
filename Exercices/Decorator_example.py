#This is an example for Decorators
import time

def timer(name):
    print("Use of function : {name}".format(name=name))
    def decorator_timer(function):
        print("Timer Called")
        def function_modified(nb_iter):
            start = time.time()
            function_called = function(nb_iter)
            end = (time.time() - start)/1000
            print("function finished in {0} s".format(end))
            return function_called
        return function_modified
    return decorator_timer

@timer(name="This is a test decorateur")
def function(nb_iter):
    result = 0
    for i in range(0, nb_iter):
        result = result + i
    print(result)

if __name__ == '__main__':
    NB_LAUNCH = 5
    for elem in range (1, NB_LAUNCH):
        function(elem)
