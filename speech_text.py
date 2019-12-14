import speech_recognition as sr

r = sr.Recognizer()

audio = '6 People/6.flac'

with sr.AudioFile(audio) as source:
	audio = r.record(source)
	print('Processing')

try:
	value = r.recognize_google(audio)
	file = open("6.txt", "a")
	file.write(value)
	print('Finished Processing')
	print(value)

except Exception as e:
	print(e)
