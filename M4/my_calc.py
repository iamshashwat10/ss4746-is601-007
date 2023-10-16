class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans
    """
    UCID: ss4746
    Date: 10-14-2023
    Description: This method adds two numbers or the previous result (stored in 'ans') to a given number and updates 'ans' with the result.
    If 'num1' is 'ans', it adds 'ans' to 'num2' and stores the result in 'ans'. If 'num1' is a number, it converts 'num1' and 'num2' to numbers,
    adds them, and stores the result in 'ans'.
    
    :param num1: Either a number or the string 'ans' to use the stored result.
    :param num2: The second number to be added.
    
    :return: The result of the addition operation, stored in 'ans'.
    """

    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    """
    UCID: ss4746
    Date: 2023-10-15
    Description: This method subtracts two numbers or the previous result (stored in 'ans') from a given number and updates 'ans' with the result.

    :param num1: Either a number or the string 'ans' to use the stored result.
    :param num2: The second number to be subtracted.
    
    :return: The result of the subtraction operation, stored in 'ans'.
    """

    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans
    """
    UCID: ss4746
    Date: 2023-10-15
    Description: This method multiplies two numbers or the previous result (stored in 'ans') with a given number and updates 'ans' with the result.

    :param num1: Either a number or the string 'ans' to use the stored result.
    :param num2: The second number to be multiplied.
    
    :return: The result of the multiplication operation, stored in 'ans'.
    """

    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2
        return self.ans

    """
    UCID: ss4746
    Date: 2023-10-15
    Description: This method divides two numbers or the previous result (stored in 'ans') by a given number and updates 'ans' with the result.
    If 'num1' is "ans," it divides 'ans' by 'num2' and stores the result in 'ans'. If 'num1' is a number, it converts 'num1' and 'num2' to numbers,
    performs the division, and stores the result in 'ans'. It also handles the case where 'num2' is 0 and prints an error message.

    :param num1: Either a number or the string 'ans' to use the stored result.
    :param num2: The second number to be used as the divisor.
    
    :return: The result of the division operation, stored in 'ans'.
    """

if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?")
    calc = MyCalc()
    #print(calc)
    if iSTR == "yes":
        while is_running:
            iSTR = input("What is your eq:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("Your eq was " + str(iSTR))
                if "+" in iSTR:
                    nums = iSTR.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in iSTR:
                    nums = iSTR.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))

                elif "*" in iSTR or "x" in iSTR:
                    nums = iSTR.split("*") if "*" in iSTR else iSTR.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))
                # must be done last so negative numbers work
                elif "-" in iSTR:
                    nums = iSTR.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("R is " + str(r))




    else:
        print("Good bye")
        is_running = False