import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser

sys = pyttsx3.init()
sys.setProperty("rate",130)
r = sr.Recognizer()

runnig = True   #checks if program is running
is_in = False   #checks if the user has logged in by clling jarvis
type_error = False  # if some speaks nothing then there comes a type error while breaking a string. THIS BOOLEAN HANDLES that PROBLEM


# talk back system
def speak(str):
    sys.say(str)
    sys.runAndWait()

# closing the program
def power_kill():
    global runnig
    runnig =False

# getting command from user
def get_command():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  
            r.dynamic_energy_threshold = True 
            print("Say something")
            
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.upper()
            print(text)
            return text
    except:
        global type_error
        type_error = True 

# checking the valid commands
def search_command(command):
    call_ups =['JARVIS','HEY JARVIS','OK JARVIS','HELLO JARVIS','JARVIS YOU THERE', 'JARVIS KYA TUM HO','JARVIS SHURU HO JAO']
    endings = ['THANK YOU JARVIS', 'THANK YOU','SUKRIYA JARVIS']
    yt = ['PLAY','JARVIS BAJAO','BAJAO']
    search_words = ["WHO IS","WHAT IS", "WHAT ARE", "WHO ARE"]
    if(command in call_ups):
        boot_up()
    if(is_in):          # checking if the user is logged in otherwise youtube search , google search or shut down function will not work
        if(command in endings):
            shut_down()
        if(type_error == False):
            if(yt[0] in command or yt[1] in command or yt[2] in command): #here in the loop we are checking something within a string, so if the string is null it will throw a type error, therefore I used that boolean variable
                yt_search(command)
            elif(search_words[0] in command or search_words[1] in command or search_words[2] in command or search_words[3] in command):
                g_search(command)
    else:
        pass

# this will help in logging in
def boot_up():
    speak("Hello Sir!!!")
    global is_in
    is_in = True

# closing the program with a nice message
def shut_down():
    speak("Its a pleasure sir !")
    power_kill()

# for youtube search
def yt_search(command):
    song1 = command.replace('PLAY','')
    song2 = song1.replace('JARJIS','')
    song = song2.replace('BAJAO','')            
    speak('playing ' + song + ' on youtube')
    pywhatkit.playonyt(song)
    speak("Enjoy your music Sir")
    power_kill()

# for google search
def g_search(command):
    string = command.lower()
    string1 = string.replace("who is","")
    string2 = string1.replace("what is","")
    string3 = string2.replace("what are","")
    string3 = string3.replace("who are","")
    keyword = string3.replace(" ","+")
    
    url = "https://www.google.com/search?q="+keyword+"&start="+str(1)

    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(url)
    speak("I have googled "+string3+ " for you sir!")
    power_kill()

# function for running
def run():
    while(runnig):
        command =  get_command()
        search_command(command)

if __name__ == "__main__":
    run()
