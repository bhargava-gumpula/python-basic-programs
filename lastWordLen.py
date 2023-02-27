def lastWordLen(string):
        list = string.split(" ")
        print(len(list[len(list)-1]))

string = input("Enter your string : ")        
lastWordLen(string)
