class Pattrens:
    
    designs = [ "1) Square","2) Triangle","3) All Shapes"]
    triangle =['1) Right Half Triangel','2) Left Half Triangel','3) Equelateral Triangel']
    
    def __init__(self) -> None:
        print("welcome to my Pattren Generator!!!!")
        print("created by @Cyberbyte0")
        self.controls()


    def get_inputs(self):
        for i in (self.designs):
            print(i)
        self.shapes(self.get_shape(),self.get_height(),self.get_char())


    def get_shape(self):
        self.shape = input("select shape/number from the above: ").lower()
        if self.shape not in '123':
            return self.get_shape()
        return self.shape

    def get_height(self):
        self.height = int(input('Enter height: '))
        if self.height <= 0:
            return self.get_height()
        return self.height

    def get_char(self):
        self.char = input("Enter your desierd char or num: ")[0]
        return self.char


    def all_shapes(self, height, char):
        self.square( height,char)
        for model in range (1,4):
            self.triangels(str(model),height,char)


    def shapes(self,shape,height,char):
        print(type(shape), shape)
        print(type(height),height)
        print(type(char),char)
        if shape == "square" or shape == '1':
            self.square(height, char)

        elif shape == "triangle" or shape == '2':
            for i in self.triangle:
                print(i)
            model = input("Select the  Number for the model of Triangle: ").lower()
            self.triangels(model ,height,char)

        elif shape == "ALL shapes" or shape == '3':
            self.all_shapes(height, char)

        else:
            print("invalid selections for shape")
            self.controls()


    def square(self, height,char,):
        for input in range(height):
            print(char * height)
        
            
    def triangels(self,model,height,char):
        if model == 'Right Half Triangel' or model == '1':
            print("Right Half Triangel")
            for input in range(1,height+1):
                print(char * input)

        elif model == 'Left Half Triangel' or model == "2":
            print("Left Half Triangel")
            for input in range (1, height+1):
                print((" " * (height-input)) + (char * input))
                
        elif model == 'Equalateral Triangle' or model == '3':
            print("Equelateral Triangel")
            for input in range(1,(height*2)):
                if input % 2 != 0:
                    print( ( " " * (height - (input//2))) + char * input)

        else:
            print("invalid selection")
            self.controls()


    def controls(self):
        start = input("Enter '1' or 'start' to continue, '0' or 'End' to quit: ")

        if start == '1' or start =="start":
            self.get_inputs()
            return self.controls()

        else:
            print("Thank you ")
            quit()
                    
            
    
Pattrens()

