class FunString:
    def __init__(self, string, mode):
        self.string = string
        self.mode = mode

    def modeCatagory(self):
        if self.mode == "1":    # 1 : Check size of string
            return len(self.string)

        elif self.mode == "2":  # 2 : Swap lettercase
            ans = ""
            for i in self.string:
                if 'a' <= i <= 'z':  # Lower to Uppercase
                    ans = ans + chr((ord(i) - 32))
                else:  # Upper to Lowercase
                    ans = ans + chr((ord(i) + 32))
            return ans

        elif self.mode == "3":  # 3 : Reverse string
            reversedString = ""
            for i in self.string:
                reversedString = i + reversedString
            return reversedString
            
        elif self.mode == "4":  # 4 : Remove duplicate characters
            lis = ""
            for char in self.string:
                if char not in lis:
                    lis += char
            return lis
            
        else:   # when input is not 1-4
            return "Try Again! Input (Number of Function) 1-4 ONLY!"

    def __str__(self):
        return "{}".format(self.modeCatagory())


if __name__ == "__main__":
    inputList = [x for x in input("Enter String and Number of Function : ").split()]
    s1 = FunString(inputList[0], inputList[1])
    print(s1)
