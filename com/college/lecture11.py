"""
Chapter 4: Python Function.

Syntax to create a function:    def functionName():
                                    instructions..
                                    instructions..
                                    instructions..

Syntax to call a function:  functionName()

Syntax to create a parameterized function: def functionName(parameter1, parameter2..)
                                                print(parameter1," ", parameter2)

Syntax to call a parameterized function: functionName(1,2)
* Here we can pass a value ("abc"), a variable (myName) and an expression (1+1) as argument.

Return statement: Easy.

Global and Local variable: I'm not going to explain this.

Different Types of Arguments:
1. Required Argument: Compulsorily pass the number of arguments which is same
                      as the number of parameters.
Example: def function(prm1, prm2, prm3):
            blah blah blah..
         function(arg1, arg2, arg3) --> Here we have to pass 3 arguments or we'll get an error.


2. Default Argument: If someone doesn't pass the argument for a parameter then we can give a
                     default value to the parameter and it will use that value just in case.
Example: def function(prm1, prm2 = 10):
            blah blah blah..
         function(prm1) --> It is okay to pass only 1 argument here.


3. Keyword Argument: If someone wants to change the order of parameters they can use this way.
                     Here we have to pass argument with name and value for it to get assigned
                     to the parameter we want it to.
Example: def function(a,b):
            blah blah blah..
         function(b=20, a=10) --> Now the value of b will get assigned to b and value of a to a.


4. Variable Length Argument: When we don't know how many arguments will be passed we can use this.
Example: def function(*prm1):  --> Assuming prm1 is a List.
            for var in prm1:
                print(var)

         function(arg1, arg2, .., argN)

"""



def myFirstPythonFunction():
    print("This is the first line in my function.")
    print("This is the second line in my function.")
    print("This is the third line in m function.")


myFirstPythonFunction()
myFirstPythonFunction()



def myFirstPythonFunctionWithParameters(rollNumber, name, password):
    print("ID is:", rollNumber)
    print("Name is:", name)
    print("Password is:", password)



myName = "Gaurav"

# The method below passes an expression, a variable and a value as argument.
myFirstPythonFunctionWithParameters(1+1, myName, "mainahibataunga")



def myFirstFunctionWithReturnStatement(number1, number2):
    return number1+number2



print("Addition:", myFirstFunctionWithReturnStatement(1, 2))

globalVariable = "Gaurav"



def testFunction(globalVariable):
    print(globalVariable)



testFunction("ABC")



def swapNumbers(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    print("Number after swapping:\n number1 = ", number1, " number2 = ", number2)


number1 = 10
number2 = 20
print("Number before swapping:\n number1 = ", number1, " number2 = ", number2)
swapNumbers(number1, number2)
