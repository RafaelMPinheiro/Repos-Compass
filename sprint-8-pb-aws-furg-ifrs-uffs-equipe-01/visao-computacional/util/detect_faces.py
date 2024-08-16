from util.get_emotion import get_emotion

def detect_faces(imageName, bucket, client):

    try:
        response = client.detect_faces(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": imageName
                }
            },
            Attributes=['EMOTIONS']
        )
        faces = []
        for fc in response['FaceDetails']:
            cassified_emotion, emotion_confidence = get_emotion(fc['Emotions'])
            faces.append({
                'position':{
                    "Height": fc['BoundingBox']['Height'],
                    "Left": fc['BoundingBox']['Left'],
                    "Top": fc['BoundingBox']['Top'],
                    "Width": fc['BoundingBox']['Width']
                },
                "classified_emotion": cassified_emotion,
                "classified_emotion_confidence": emotion_confidence 
            })
        if(len(faces) == 0):
            faces.append({
                'position':{
                    "Height": None,
                    "Left": None,
                    "Top": None,
                    "Width": None
                },
                "classified_emotion": None,
                "classified_emotion_confidence": None 
            })
        return faces
    except Exception as e:
        raise e

