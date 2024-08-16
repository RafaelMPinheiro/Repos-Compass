def detect_labels(imageName, bucket, client):

    try:
        response = client.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": imageName,
                }
            },
            MaxLabels=10,
            MinConfidence=90
        )

        labels = []
        for label in response['Labels']:
            # print("Label: " + label['Name'])
            # print("Confidence: " + str(label['Confidence']))
            labels.append({
                "Confidence": label['Confidence'],
                "Name": label['Name']
            })

        return labels
    except Exception as e:
        raise e
