def get_emotion(Emotion):
    mvEmotionName = ''
    confidence = 0

    for emot in Emotion:
        if(emot['Confidence'] > confidence):
            mvEmotionName = emot['Type']
            confidence = emot['Confidence']
            
    return mvEmotionName, confidence