import speech_recognition as sr

r = sr.Recognizer()

def record_text():

    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            mytext = r.recognize_google(audio2)

            return mytext

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return "Request_Error"
        
    except sr.UnknownValueError:
        print("Unknown Value Error")
        return "Unknown_Value_Error"
    
if __name__ == "__main__":
    
    speech_to_text_output = record_text()
    print(speech_to_text_output)