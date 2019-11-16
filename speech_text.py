import speech_recognition as sr

r = sr.Recognizer()

audio = 'file_name.type'

with sr.AudioFile(audio) as source:
	audio = r.record(source)
	print('Processing')

try:
	value = r.recognize_google(audio)
	file = open("file_name.txt", "a")
	file.write(value)
	print('Finished Processing')
	print(value)

except Exception as e:
	print(e)
