import speech_recognition
import pyttsx3
from datetime import datetime
from datetime import date

#Thư viện pyttsx3 được cài từ nguồn bên ngoài

#Khởi tạo các biến
mouth = pyttsx3.init()
bot_ear = speech_recognition.Recognizer() 
bot_brain = "" 
num_ques = 0      #khởi tạo số câu hỏi

while True:
      #Dùng vòng lặp để đối thoại liên tục

            #Máy nhận dạng lời nói
            with speech_recognition.Microphone() as mic:
                  print("Selena: I'm listening")
                  audio = bot_ear.listen(mic) 

            print("Robot: ...")
            try:
                   you = bot_ear.recognize_google(audio) 
            except:
                   you = ""

               #Nếu không nhận được lời nói thì hiển thị rỗng

            print("you: " + you)

               #Khởi tạo một số câu trả lời của máy 
               #Trích từ file may_hieu.py


            if you == "": 
                  bot_brain = "I can't hear you. Try again."
            elif "hello" in you:
                  bot_brain = "xin chao"
            elif "how is your today" in you:
                  bot_brain = "I'm on my own. How's about you?"
                  print("Elisa: " + bot_brain)
                  mouth.say(bot_brain)
                  mouth.runAndWait()
                        #Nhận diện câu trả lời
                  with speech_recognition.Microphone() as mic:
                        audio = bot_ear.listen(mic) 
                  try:
                        you = bot_ear.recognize_google(audio) 
                  except:
                        you = ""
                  if 'fine' in you or 'good' in you:
                        bot_brain = 'that sounds great'
                  elif 'bad' in you or 'sad' in you:
                        bot_brain = 'what is yor matter, my friend?'
                  else: 
                        bot_brain = 'sorry, can you say again?'
            

            elif "today" in you and "what" in you:
                  today = date.today()
                  bot_brain = today.strftime("%B %d,%Y")
            elif "time" in you:
                  now = datetime.now() 
                  bot_brain = now.strftime("%H hours %M minutes %S seconds")
            print("Selena: " + bot_brain)

            #Máy tính phản hồi
            #Trích từ file noi.py

            
            mouth.say(bot_brain)
            mouth.runAndWait()
            if "goodbye" in you:
                  bot_brain = "Bye. See ya" 
                  print("Selena: " + bot_brain)
                  mouth.say(bot_brain)
                  mouth.runAndWait()
                  break
                        #nếu nói bye thì thoát vòng lặp, kết thúc ct


      #py Selena.py