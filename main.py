with open('Script.txt', encoding = 'utf-8') as Script:
	String = Script.read()
	String = String.split(' ')
	print(String)

	with open('Test.txt', encoding = 'utf-8') as Test:
		Check = Test.read()
		Check = Check.split(' ')
		print(Check)

		result = any(elem in Check for elem in String)

		re = []
		for element in Check:
			if element in String:
				re.append(element)
		print(re)
		print('Accuracy: ', len(re), '/', len(String))
		print('Percentage:', (len(re)/len(String))*100, '%')
