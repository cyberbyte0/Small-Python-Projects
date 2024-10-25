import pyttsx3
class Talk_Bot:

    def __init__(self) -> None:
        engine =pyttsx3.init()     
        print("Welcome to my Talk Bot...")
        print('created by @cyberbyte0...')
        say = engine.say
        self.get_inputs(engine,say)


    def get_inputs(self,engine,say):
        self.get_gender(engine)
        self.get_speed(engine)
        self.talk(say,engine)
        

    def get_gender(self,engine):
        print("select voice type")
        voice = input('Enter M for Male and F for Female: ').lower()
        if voice == 'm':
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', voices[0].id)
        elif voice =='f':
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', voices[1].id)
        else:
            print("select again...")
            self.get_gender(engine)

        
    def get_speed(self,engine):                          
        engine.setProperty('rate', 120)


    def talk(self,say,engine):
        while True:
            print('Type 0 to quit or 1 to change settings')
            msg = input('Enter text to speak: ')
            
            if msg == '0':
                break
            elif msg == '1':
                self.get_inputs(engine,say)
            else:
                say(f'{msg}')
                engine.runAndWait()
        

Talk_Bot()