import cv2
import face_recognition

encoding_wajah = []
file_path = "./p.jpeg"
foto = face_recognition.load_image_file(file_path)
encoding_foto = face_recognition.face_encodings(foto)[0]
encoding_wajah.append(encoding_foto)
video = cv2.VideoCapture(0)


def wajah() :
    bataswaktu = 0
    hitung = 0
    while True:
        ret, frame = video.read()
        if not ret :
            print("tidak bisa membaca frame")
            break

        lokasi_wajah = face_recognition.face_locations(frame)
        encode = face_recognition.face_encodings(frame, lokasi_wajah)

        if len(lokasi_wajah) == 0 :
            bataswaktu += 1
            print(f"bataswaktu anda {7 - bataswaktu}")
            if bataswaktu == 7 :
                video.release()
                return False

        for (top, right, bottom, left), encoding_wajah in zip(lokasi_wajah, encode) :
            matches = face_recognition.compare_faces([encoding_foto], encoding_wajah)
            if True in matches :
                cv2.rectangle(frame, (left,top), (right,bottom), (0,0,255), 2)
                cv2.putText(frame, "MENGONFIRMASI", (left - 35, top - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9 , (0,0,255),2)
                cv2.putText(frame, "WAJAH", (left, top - 10), cv2.FONT_HERSHEY_COMPLEX, 0.9 , (0,0,255),2)
                hitung += 1
                print(hitung)
                if hitung == 5 :
                    video.release()
                    return True  
  
            elif True not in matches :
                cv2.rectangle(frame, (left,top), (right,bottom), (0,0,255), 2)
                cv2.putText(frame, "TIDAK", (left, top - 35), cv2.FONT_HERSHEY_COMPLEX, 0.9 , (0,0,255),2)
                cv2.putText(frame, "DIKETAHUI", (left, top - 10), cv2.FONT_HERSHEY_COMPLEX, 0.9 , (0,0,255),2)
                bataswaktu += 1
                print(f"bataswaktu anda {7 - bataswaktu}")
                if bataswaktu == 7 :
                    video.release()
                    return False

        cv2.imshow("VIDEO", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break



print(wajah())

