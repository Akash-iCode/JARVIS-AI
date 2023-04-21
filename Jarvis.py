from Brain.AiBrain import replyBrain
from Body.Listen import MicExecution
print(">> STARTING JARVIS : WAIT FOR FEW SECONDS")
from Body.Speak import Speak
from Features.Clap import Tester
from Brain.QnA import questionANSWERS
print(">> STARTING JARVIS : GETTING DEPEPNDANCIES READY")
from Main import MainTaskExecution
from WakeWord.wakeWordChecker import isHotWordCalled
from WakeWord.decrypt  import SecretsDecryptor
from WakeWord.chimeSounds import *
# Create a SecretsDecryptor instance with the decryption key (if it's different than the default key)
key = b'1234567890123456'
decryptor = SecretsDecryptor(key)

# Decrypt the secrets from the file
secrets = decryptor.decrypt_secrets('porcupineAccess.txt')

# Use the decrypted secrets as needed
porcupine_api_key = secrets['api_key']
wake_words = secrets['wakeWords']
print(wake_words)
accessKey= porcupine_api_key
keyWords = ["jarvis", "hey google", "alexa", "hey siri", "ok google"]

hotword_detector = isHotWordCalled(access_key=accessKey, keywords=keyWords)

def MainExecution():
    Speak("Hello Sir!")
    Speak("I'm JARVIS, your personal assistant ready to serve you")
    print("")
    while True:
        if hotword_detector.is_keyword_detected():
            play_success_sound()
            Data = MicExecution()
            Data = str(Data)

            ValueReturn = MainTaskExecution(Data)

            if ValueReturn == True:
                pass
            elif len(Data)<3:
                pass
            elif "turn on the tv" in Data or "open the tv" in Data:
                play_info_sound()
                Speak("OK !! Turning on the Living room tv")
                pass
            elif "how many" in Data :
                play_info_sound()
                Reply = questionANSWERS(Data)
                Speak(Reply)
            elif "go offline" in Data:
                play_info_sound()
                Speak("See you later, hasta la vista, SIR !")
                exit()
            elif Data == "skip" or Data == "pass" or  Data == "ignore it" or Data == "nothing" :
                pass
                play_info_sound()
            else:
                play_info_sound()
                Reply = replyBrain(Data)
                Speak(Reply)
 
def ClapDetect():
    query=Tester()   
    if "True-Mic" in query:
        print("")
        print(">> CLAP DETECTED !! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()