class EmptySentenceError(Exception):
    pass

try:
    sentence = input("Enter anything: ").lower()

    if not sentence.strip():
        raise EmptySentenceError("Sentence cannot be empty")

    vowel = ['a', 'e', 'i', 'o', 'u']
    
    longestWords = [] 
    frequentWord = {}

    digitCounter = 0
    vowelCounter = 0
    consonantCounter = 0
    spaceCounter = 0

    longestWordFinder = 0

    charCounter = len(sentence)
    wordCounter = sentence.split()

    for char in sentence:
        lowerChar = char.lower()
        if lowerChar.isalpha():
            if lowerChar in vowel:
                vowelCounter += 1
            else :
                consonantCounter += 1
        elif lowerChar.isdigit():
            digitCounter += 1
        elif lowerChar.isspace():
            spaceCounter += 1

    cleanedWords = []

    for word in wordCounter:
        cleanedWord = word.strip(".,!?;:\"'()[]{}")
        if cleanedWord :
            cleanedWords.append(cleanedWord)

    uniqueWordCounter = set(cleanedWords)

    for word in cleanedWords:
        if(len(word) > longestWordFinder):
            longestWordFinder = len(word)
            longestWords = [word]
        elif(len(word) == longestWordFinder):
            if word not in longestWords:
                longestWords.append(word)

    for word in cleanedWords:
        if word in frequentWord:
            frequentWord[word] += 1
        else:
            frequentWord[word] = 1

    print("\nWords Frequency :- ")
    for word, count in frequentWord.items():
        print(word, ":", count)

    print("\nFinal Report :- ")
    print("-" * 35)
    print(f"{'Thing':<22}Amount")
    print("-" * 35)
    print(f"{'Characters':<22}{charCounter}")
    print(f"{'Words':<22}{len(wordCounter)}")
    print(f"{'Vowels':<22}{vowelCounter}")
    print(f"{'Consonants':<22}{consonantCounter}")
    print(f"{'Digits':<22}{digitCounter}")
    print(f"{'Spaces':<22}{spaceCounter}")
    print(f"{'Unique Words':<22}{len(uniqueWordCounter)}")
    print(f"{'Longest Words':<22}{', '.join(longestWords) if longestWords else 'None'}")
    print(f"{'Longest Word Length':<22}{longestWordFinder}")
    print(f"{'Frequent Words':<22}{len(frequentWord)}")

    print("-" * 35)

except EmptySentenceError as e:
    print("\nError : ",e)
