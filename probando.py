import cv2
import face_recognition
#image for comparison
#imagen para realizar comparación
image = cv2.imread("C:/Users/cecil/Desktop/probando_face_recognition/images/foto perfil (2).jpg")
face_loc = face_recognition.face_locations(image)[0]
 #print("face_loc:", face_loc)
face_image_encondings = face_recognition.face_encodings(image, known_face_locations=[face_loc])[0]
  #print ("face_image_encondings", face_image_encondings)

#cv2.rectangle(image, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0))
#cv2.imshow("Image",image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()




cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
     ret, frame = cap.read()
     if ret == False: break
     frame = cv2.flip(frame, 1)
     
     face_locations = face_recognition.face_locations(frame)
     if face_locations != []:
         for face_location in face_locations:
              face_frame_encondings = face_recognition.face_encodings(frame, known_face_locations=[face_loc])[0]
              result = face_recognition.compare_faces([face_frame_encondings], face_image_encondings)
              print("result:", result)
              
              cv2.rectangle(frame, (face_location[3], face_location[0]),( face_location[1], face_location[2]),(0, 255, 0),2)
             
     cv2.imshow("Frame", frame)
     k = cv2.waitKey(1)
     if k == 27 & 0xff:
          break
      
cap.release()
cv2.destroyAllWindows()
