def learn(message):
    '''learns from messages'''
    vocabDict = load_obj("vocabDict")
    chainList = []
    message = killPunc(message).lower().split()#removes punctuation and splits string into a list
    if len(message) >= 3:
        message.append("<stop>")
        for i in range(len(message)-2):
            chainList.append(message[i:i+3]) #creates list of chains
        
        for chain in chainList: #splits chains into dict
            if not (chain[0],chain[1]) in vocabDict:
                vocabDict[(chain[0],chain[1])] = [chain[2]]
            else:
                vocabDict[(chain[0],chain[1])].append(chain[2])
        
        save_obj(vocabDict, "vocabDict") 
        return vocabDict
    else: pass

def speak(message):
    '''takes last two words of the message and generates statement'''
    vocabDict = load_obj("vocabDict")
    message = message.split()
    word1, word2, = message[-2], message[-1] #takes last two words of previous message
    for i in range(2): #sets up chain and filters out seed words
        nextWord = random.choice(vocabDict[(word1,word2)])
        word1, word2 = word2, nextWord
        
    statement = word1 + ' ' + word2 #what eight will eventually say
        
    while nextWord != "<stop>":
        nextWord = random.choice(vocabDict[(word1,word2)])
        statement+=' '+nextWord
        word1, word2 = word2, nextWord
        
    return statement[:-7] #returns message minus "<stop>"
