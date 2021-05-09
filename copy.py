import pyttsx3
import speech_recognition as sr
import smtplib
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send_mail(to, subject, body):
    your_email = "your_email"
    email_pswd = "your_password"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("your_email", "your_password") # please fill this field
        server.sendmail("your_email", to,
                        f"Subject: {subject}\n\n{body}")
        server.quit()

    except Exception as e:
        print(e)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print("Reconizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said :- {query}")

    except Exception as e:
        speak(".")
        return "none"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'send email' in query:

            speak("Alright to whom? Tell me ! !")
            whom = takeCommand().lower()
            if "second account" in whom or "myself" in whom:
                to = "email address"  #fill the required field
                speak("What's the subject of the mail?")
                subject = takeCommand().lower()
                speak("speak the body of the mail?")
                body = takeCommand().lower()
                send_mail(to, subject, body)

        elif "open the gmail" in query:
            speak("opening gmail") 
            webbrowser.open_new_tab('www.gmail.com')

            
    
    

 

