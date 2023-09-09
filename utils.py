class utils:
    
   #Function takes an integer and returns it reversed (I think reverse the order of digits)
    def reversed (self, num):

        #Check the type and return invalid if not int
        if (type(num) != int):
            print("Incorrect data type passed to function")
            return None

        #First let us get the digits
        digits = []
        
        #convert the integer into a string so we can iterate through digits
        num = str(num)

        #Iterate and collect the digits
        for letter in num:
            digits.append(letter)

        #Reverse the list
        digits.reverse()

        #Join the reversed digits
        reversedNum = "".join(digits)
        
        return int(reversedNum)
    
    #Function that takes an int and returns it in binary and octal format
    def formatter(self, num):

        #Check the type and return invalid if not int
        if (type(num) != int):
            print("Incorrect data type passed to function")
            return None
        
        #Now we can return a tuple for the number in binary and octal format
        return (bin(num), oct(num))


