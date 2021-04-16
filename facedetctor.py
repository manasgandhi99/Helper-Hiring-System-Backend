import face_recognition
import numpy as np
import requests
import urllib.request 
from urllib.request import Request, urlopen


face_encodings = []

def give_face_encoding(url):
    face_locations = []
    print("Requests tak pohocha!!!!!!!!!!!!!!!")
    # response = requests.get(url)
    # file = open("test.jpg", "wb")
    # file.write(response.content)
    urllib.request.urlretrieve(url, "test.jpg")
    test_img = face_recognition.load_image_file("test.jpg")
    face_locations = face_recognition.face_locations(test_img)

    #Create face encodings of detected faces
    single_face_encoding = face_recognition.face_encodings(test_img, face_locations)
    face_encodings.append(single_face_encoding[0])
    print("Encodings store hua!!!!!!!!!!!!!!!")

def hello(url, frame1, frame2, frame3):
    print(url)
    url= url[:108] + '%2F' + url[109:]
    frame1= frame1[:108] + '%2F' + frame1[109:]
    frame2= frame2[:108] + '%2F' + frame2[109:]
    frame3= frame3[:108] + '%2F' + frame3[109:]
    # frame5= frame5[:91] + '%2F' + frame5[92:]

    print("Achchha URL:\n"+url)
    print("Achchha frame1:\n"+frame1)
    print("Achchha frame3:\n"+frame3)
    print("Achchha frame2:\n"+frame2)
    # print("Achchha frame5:\n"+frame5)

    give_face_encoding(url)
    give_face_encoding(frame1)
    give_face_encoding(frame2)
    give_face_encoding(frame3)
    # give_face_encoding(frame5)
    print("Encodings nikal gaye")
    # print(len(face_encodings))  

    doc_encoding = face_encodings[0]
    face_encodings.pop(0)
    print("Doc encoding alag se nikal gaya")
    print("Doc encoding: ",doc_encoding)
    print("Face encodings: ", face_encodings)
        
    matches = face_recognition.compare_faces(face_encodings, doc_encoding, tolerance = 0.6)
    print("compare ho gaya")
    
    name = 0
    threshold = 0.51
    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(face_encodings, doc_encoding)
    print("distance nikal gaya")
    
    best_match_index = np.argmin(face_distances)
    if face_distances[best_match_index] <= threshold: 
        if matches[best_match_index]:
            name = 1
    print(name)    
    print("Done")

    return name


#http://localhost:5000/home?doc=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2FFurrr.jpg?alt=media&token=1f8c10b3-6b71-4c99-939b-7fa290509fda&frame1=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai1.png?alt=media&token=97a170f5-93df-4367-9492-ab857dee1c47&frame2=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai2.png?alt=media&token=eb6281b6-e523-4c14-9f18-cfd759ff8e7e&frame3=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai3.png?alt=media&token=a2363af5-9d30-45f5-b93a-b16d54b4894e

# https://e12cd4a02385.ngrok.io/home?doc=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2FFurrr.jpg?alt=media&token=1f8c10b3-6b71-4c99-939b-7fa290509fda&frame1=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai1.png?alt=media&token=97a170f5-93df-4367-9492-ab857dee1c47&frame2=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai2.png?alt=media&token=eb6281b6-e523-4c14-9f18-cfd759ff8e7e&frame3=https://firebasestorage.googleapis.com/v0/b/e-kyc-34a84.appspot.com/o/100560013326805107879%2Fsam-bhai3.png?alt=media&token=a2363af5-9d30-45f5-b93a-b16d54b4894e
# ngrok http 5000

# https://firebasestorage.googleapis.com/v0/b/helper-hiring-backend.appspot.com/o/frame%40gmail.com%2Fimage0?alt=media&token=0f4fc0b9-faac-4277-ab0d-0093445d21eb

# https://firebasestorage.googleapis.com/v0/b/helper-hiring-backend.appspot.com/o/koI1Nkjkw6S084aoHwJAQeQA91D2%2Fimage0?alt=media&token=aa437411-9553-4264-b847-f76b70580b63