import speech_recognition as sr
from difflib import SequenceMatcher

r = sr.Recognizer()

language = input("Which language would ou like to prefer? (eng or tr)  \n")

if(language=="eng"):
    music = input("Which music would you like to choose? \n (brunomars.wav - imaginedragons.wav) \n ")
    with sr.AudioFile(music) as source:
     voice = r.listen(source)

    try:
          text = r.recognize_google(voice, language = "en-US")                
          print(text)
          lyrics = open("lyrics.txt", "w")
          lyrics.write(text)
          lyrics.close()
          first = open("lyrics.txt").read()
          
          if(music=="brunomars.wav"):
            second = open("truthlyrics.txt").read()
            print(f"Both are {SequenceMatcher(a=first, b=second).ratio()*100} % similar")
          if(music=="imaginedragons.wav"):
            second = open("truthlyrics2.txt").read()
            print(f"Both are {SequenceMatcher(a=first, b=second).ratio()*100} % similar")

    except:
           print('error')

if(language=="tr"):
    music = input("Which music would you like to choose? \n (sagopakajmer.wav - edis.wav) \n")
    with sr.AudioFile(music) as source:
     voice = r.listen(source)

    try:
          text = r.recognize_google(voice, language = "tr-TR")                
          print(text)
          lyrics = open("lyricstr.txt", "w")
          lyrics.write(text)
          lyrics.close()
          first = open("lyricstr.txt").read()

          if(music=="sagopakajmer.wav"):
            second = open("truthlyricstr.txt").read()
            print(f"Both are {SequenceMatcher(a=first, b=second).ratio()*100} % similar")
          if(music=="edisnew.wav"):
            second = open("truthlyricsedis.txt").read()
            print(f"Both are {SequenceMatcher(a=first, b=second).ratio()*100} % similar")

    except:
           print('error')


