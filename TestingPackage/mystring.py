class MyString():
    def __init__(self, str=""): # initializes  the object
        self.str=str

    #Returns the current string.

    def getString(self):
        return self.str

    #Returns a string that consists of all and only the vowels in the current string.
    #Only letters a, e, i, o, and u (both lower and upper case) are considered vowels.
    #The returned string contains each occurrence of a vowel in the current string.
    def getVowels(self):
        lowercase=self.str
        lowercase=lowercase.lower()
        vowels=""
        count=len(lowercase)

        for a in range(0,count):
            if lowercase[a]=='a'or lowercase[a]=='e' or lowercase[a]== 'i' or lowercase[a]=='o' or lowercase[a]== 'u':
                vowels=vowels+self.str[a]
        return vowels

    #Returns a string that consists of the substring between start and end indexes (both included) in the current string.
    #Index 1 corresponds to the first character in the current string.'''
    def getSubstring(self,start,end):
        sub=""
        try:
            for a in range(start-1,end):
                sub=sub+self.str[a]
        except IndexError:
            print("Index out of bounds")
        return sub

    #Breaks the string down, and returns it as a character string
    def getCharList(self):
        thelisttorulethemall=[]
        counter=len(self.str)
        print(counter)
        for w in range (0,counter):
            thelisttorulethemall.append(self.str[w])
        return thelisttorulethemall

    #Returns the index of the first occurrence of a character in the current string.
    #Index 1 corresponds to the first character in the current string.
    # return 0 if no match is found
    def indexOf(self,c):
        indexthing = ""
        try:
            for a in (0,c):
                indexthing = self.str[c-1]
        except IndexError:
            print("Index out of bounds")
        return indexthing


    # Removes all occurrences of the specified character from the current string.
    def removeChar(self,c):
        themainstring=self.str
        listcount=len(themainstring)
        theextraletters=""
        counter=0
        while counter<listcount:
            if themainstring[counter]!=c:
                theextraletters = theextraletters + themainstring[counter]
                counter = counter + 1
            else:
                counter = counter + 1

        return theextraletters


    #Invert the current string.
    def invert(self):
        backwardstext = self.str[::-1]
        return backwardstext
