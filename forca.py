word = str(input("Jogador 1, qual a palavra?"))
wordArray = []
findArray = []
errors = 0
maxErrors = 10

for i in word:
    wordArray.append(i)
    findArray.append("_ ")

def characterExists(array, tryCharacter):
    indexList = []
    for index, character in enumerate(array):
        if character.lower() == tryCharacter.lower():
            indexList.append(index)
    return indexList

while errors < maxErrors:
    print(f"{''.join(findArray)}")
    tryCharacter = str(input("Digite uma letra?"))

    if tryCharacter in findArray:
        print("Você já acertou essa letra.")
        continue

    existsCharacters = characterExists(wordArray, tryCharacter)
    if len(existsCharacters) <= 0:
        errors += 1
        print(f"Essa letra não existe na palavra. Você tem mais {maxErrors - errors} tentativas.")
        continue

    for i in existsCharacters:
        findArray[i] = wordArray[i]

    word = "".join(wordArray)
    find = "".join(findArray)

    if word == find:
        print(f"Parabéns, você acertou a palavra {word}!")
        break

if errors >= maxErrors:
    print(f"Infelizmente você perdeu, a palavra era {''.join(wordArray)}.")