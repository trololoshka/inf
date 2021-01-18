userinput = input("Введите цепочку символов из букв русского алфавита: ")
print("Принято!")
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

if userinput[-1] in alphabet: 
	index=alphabet.index(userinput[-1].lower())
	if index==len(alphabet)-1:
		index = 0
	else:
		index+=1
	lastsymbol = alphabet[index]
else :
	lastsymbol = userinput[-1]
answer =  userinput + userinput[::-1] + lastsymbol
print("Ответ: " + answer)