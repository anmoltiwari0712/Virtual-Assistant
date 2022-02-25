from ast import While #
from asyncio.windows_events import NULL  #
from urllib import response #
import speech_recognition as sr
import pyttsx3
import datetime   
import pyjokes

  

ch="y"

while ch in ["y","yes","YES","Y"]: 
    r=sr.Recognizer()
    ans="ANSWER: "
    
    with sr.Microphone() as source2:   #using microphone as source to get audio
        r.adjust_for_ambient_noise(source2, duration=0.2)
        try:
            print("Recognizing...")
            audio2=r.listen(source2)
        
            mytext=r.recognize_google(audio2)# using google to recognize
            mytext.lower()
            print("TRANSCRIPT: ",mytext)

            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate',170)
            
            if 'hello' in mytext:
                engine.say('HI THERE ITS GREAT TO TALK TO YOU')
                engine.runAndWait()
                print(ans,'HI THERE ITS GREAT TO TALK TO YOU')


            elif 'what are you doing' in mytext:
                engine.say('HELLO FROM THE CLOUD SENDING SOME GOOD THOUGHTS FOR YOU')
                engine.runAndWait()
                print(ans,'TALKING TO YOU ALWAYS MAKES ME HAPPY SIR')


            elif 'how are you' in mytext:
                engine.say('TALKING TO YOU ALWAYS MAKES ME HAPPY SIR')
                engine.runAndWait()
                print(ans,'TALKING TO YOU ALWAYS MAKES ME HAPPY SIR')


            elif 'weather' in mytext:
                engine.say('Todays forecast has mostly sunny weather')
                engine.runAndWait()
                print(ans,"TODAY'S FORECAST HAS MOSTLY SUNNY WEATHER")


            elif 'are you there' in mytext:
                engine.say('always at your service sir')
                engine.runAndWait()
                print(ans,"ALWAYS AT YOUR SERVICE SIR")


            elif 'your name' in mytext:
                engine.say('I am ALEX sir always at your service')
                engine.runAndWait()
                print(ans,"I AM ALEX SIR ALWAYS AT YOUR SERVICE")

            elif 'quote' in mytext:
                engine.say('IF YOU WANT SOMETHING YOU NEVER HAD THEN YOU MUST DO SOMETHING YOU HAVE NEVER DONE')
                engine.runAndWait()
                print(ans,"IF YOU WANT SOMETHING YOU NEVER HAD THEN YOU MUST DO SOMETHING YOU HAVE NEVER DONE")

            elif 'fun fact' in mytext:
                engine.say('WELL ALEXA IS MY ELDER SISTER')
                engine.runAndWait()
                print(ans,"WELL, ALEXA IS MY ELDER SISTER")

            elif 'who created you' in mytext:
                engine.say('A TEAM OF PASSIONATE TECH ENTHUSIASTS')
                engine.runAndWait()
                print(ans,"A TEAM OF PASSIONATE TECH ENTHUSIASTS")

            elif 'what can you do' in mytext:
                engine.say('THERES A LOT FOR EXAMPLE TRY SAYING THINGS LIKE GIVE ME A RIDDLE')
                engine.runAndWait()
                print(ans,"THERES A LOT FOR EXAMPLE TRY SAYING THINGS LIKE GIVE ME A RIDDLE")

            elif 'riddle' in mytext:    
                engine.say('What is always in front of you but cant be seen?')
                engine.runAndWait()
                print(ans,"What is always in front of you but cant be seen?")
                engine.say('your future')
                print(ans,'your future')

            elif 'voice is beautiful' in mytext:
                engine.say('THANK YOU ITS ONE OF MY BEST FEATURE!!')
                engine.runAndWait()
                print(ans,"THANK YOU ITS ONE OF MY BEST FEATURE!!")

            elif 'time' in mytext:
                time = datetime.datetime.now().strftime('%I:%M %p')
                engine.say('Current time is ' + time)
                engine.runAndWait()

            elif 'are you single' in mytext:
                engine.say('I am in a relationship with wifi')
                engine.runAndWait()
                print(ans,"I am in a relationship with wifi")


            elif 'joke' in mytext:
                engine.say(pyjokes.get_joke())
                engine.runAndWait()


            elif 'date' in mytext:
                from datetime import date 
                today = date.today()
                engine.say("Today's date is", today)
                engine.runAndWait()
                print(today)  


            
            elif 'bye' in  mytext:
                engine.say('GOOD BYE')
                engine.runAndWait()
                print(ans,"GOOD BYE")
                ch="a"
    

            

        except sr.UnknownValueError:
            engine = pyttsx3.init()
            rate = engine.getProperty('rate')
            engine.setProperty('rate',170)
            print("Did u just say something I have trouble in listening you please try again")
            engine.say('Did u just say something I have trouble in listening you please try again')
            engine.runAndWait()

            ch="D"
      

    

        












