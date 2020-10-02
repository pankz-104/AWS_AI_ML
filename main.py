import boto3
import base64
import json
import os

ACCESS_KEY='ASIAVA26GUSM2GFNL37V'
SECRET_KEY='IgU1lZbIOoSKHOe+sC991EETYJQDPtr3NGvXuX/N'
SESSION_TOKEN='FwoGZXIvYXdzEHYaDKYNSzXQS6v/jEZY8SLYAeVXz3lPmSFEMAyfCLdEemZoJYRNgAmDjgw2qwkgl3BkIt6b2hRi7beXLJKxPGofx+1igsf/eFOoWq8/WVPQVRepZbEn9kBML2l3QAt4CBns6wH6Pkk0djd82miNdPOK9735Uwxk/QU5IfWhrzR6qBAnBzWsLaHZguABixPMICQWuW+BYvmXp0N+O8S29oG6/NJhDSpvEICLmzgJY8kL+sAAGtOOx0Jb98h9JOnjnzGwKOHc54vNDi82IQcadv/LMhYE32ymDGunjSSMZxtPDilUq7xi/4W+gSiQydz7BTItwO3PMSUDlm5bsVIgJ/dVh0shPbXw+wyA6jHGlaLg5cYkgUWAy7ajxHGSmy7C'

photo = 'C:\\Users\\Pankaj\\PycharmProjects\\Rekognition\\Images\\sample1.jpg'

# Sets up the boto3 for rekognition
client = boto3.client('rekognition',
                      region_name='us-east-1',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY,
                      aws_session_token=SESSION_TOKEN
                      )

# Reads the input image and requestst the rekognition and receives the response

with open(photo, 'rb') as image:
    response = client.detect_faces(
        Image={
            'Bytes': image.read(),
        },
        Attributes=['ALL']
    )

for face in response['FaceDetails']:
    print("The detected face is between "+ str(face["AgeRange"]["Low"])+ " and "+str(face["AgeRange"]["High"])+" years old ")
    print("The person is "+str(face["Gender"]["Value"])) #1111
    face['Emotions'] = [emotion['Type']
                             for emotion in face['Emotions'] if emotion['Confidence'] > 70]
    if face['Emotions']:
        print('This face has emotions as: ', ' '.join(face['Emotions']))
    if face['Sunglasses']['Value']:
        print('This person seems to be wearing Sunglasses')
    if face['Eyeglasses']['Value']:
        print('This person seems to be wearing Eyeglasses')
    if face['Beard']['Value']:
        print('This person seems to have a Beard')