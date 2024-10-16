class Pattrens:
    
    designs = [ "1) Square","2) Triangle"]
    triangle =['1) Right Half Triangel','2) Left Half Triangel','3) Equelateral Triangel']
    
    def __init__(self) -> None:
        print("welcome to my Pattren Generator!!!!")
        print("created by @Cyberbyte0")
        self.controls()


    def get_inputs(self):
        for i in (self.designs):
            print(i)
        self.shape = input("select shape/number from the above: ").lower()
        self.shapes(self.shape)


    # def all_shapes(self, length, char):
    #     self.square( length,char)

    #     for type in range (1,4):
    #         self.triangels(type,length,char)



    def shapes(self,shape):
        length = int(input('Enter Lenght: '))
        char = input("Enter your desierd char or num: ")
        if shape == "square" or shape == '1':
            self.square(length, char)

        elif shape == "triangle" or shape == '2':
            for i in self.triangle:
                print(i)
            type = input("Select the  Number for the type of Triangle: ").lower()
            self.triangels(type ,length,char)

        else:
            print("invalid selections")
            self.controls()

    def square(self, length,char,):
        for input in range(length):
            print(char * length)
        self.controls()
            

    def triangels(self,type,length,char):
        if type == 'Right1 Half Triangel' or type == '1':
            print("Right Half Triangel")
            for input in range(1,length+1):
                print(char * input)

        elif type == 'Left Half Triangel' or type == "2":
            print("Left Half Triangel")
            for input in range (1, length+1):
                print((" " * (length-input)) + (char * input))
                
        elif type == 'Equalateral Triangle' or type == '3':
            print("Equelateral Triangel")
            for input in range(1,(length*2)):
                if input % 2 != 0:
                    print( ( " " * (length - (input//2))) + '@' * input)

        else:
            print("invalid selection")
        self.controls()


    def controls(self):
        start = input("Enter '1' or 'start' to continue, '0' or 'End' to quit: ")

        if start == '1' or start =="start":
            self.get_inputs()

        else:
            print("Thank you ")
            quit()
                    
            
    
Pattrens()

