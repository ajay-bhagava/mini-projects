def generateOriginalString(encodedString: str):
    cleanedString = encodedString[0::2]
    decodedString = ""

    for character in cleanedString:
        characterToAdd = chr(ord(character)-1)
        decodedString += characterToAdd
    
    print(decodedString)

encodedString = input("Enter an encoded string: ")
generateOriginalString(encodedString)
