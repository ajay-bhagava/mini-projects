def generateEncodedString(inputText: str):
    encodedString = ""
    for character in inputText:
        characterToInsert = chr(ord(character) + 1)
        calculatedRandomCharacter = chr(ord(character) + 5) 
        if ord(character) == 122:
            encodedString += "a"
        else:
            encodedString += characterToInsert + calculatedRandomCharacter
    print(encodedString)

# Driver Code
inputText = input("Enter some text: ")
generateEncodedString(inputText)