import cv2
import face_recognition
import numpy as np
import os
import requests
from io import BytesIO
from PIL import Image

# ------------------------------------------------------
# دالة لتحميل الصورة من رابط URL وإرجاعها كصورة OpenCV
# ------------------------------------------------------
def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

# ------------------------------------------------------
# دالة لتحميل صور الوجوه المعروفة من مجلد محلي
# وتخزين ترميز كل وجه مع اسمه
# ------------------------------------------------------
def load_known_faces(known_dir):
    known_encodings = []
    known_names = []

    for file in os.listdir(known_dir):
        path = os.path.join(known_dir, file)
        if not os.path.isfile(path):
            continue

        # تحميل الصورة وترميزها
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            known_names.append(os.path.splitext(file)[0])  # الاسم = اسم الملف بدون الامتداد
    return known_encodings, known_names

# ------------------------------------------------------
# دالة للتعرف على الوجوه في الصورة المدخلة
# ------------------------------------------------------
def recognize_faces_from_url(url, known_dir):
    # تحميل الوجوه المعروفة
    print("[INFO] Loading known faces...")
    known_encodings, known_names = load_known_faces(known_dir)

    # تحميل الصورة من الإنترنت
    print("[INFO] Loading image from URL...")
    img = load_image_from_url(url)

    # تحويلها إلى RGB لأن مكتبة face_recognition تستخدمه
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # الكشف عن مواقع الوجوه في الصورة
    face_locations = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, face_locations)

    # المرور على كل وجه في الصورة ومحاولة التعرف عليه
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # اختيار أفضل تطابق عبر المسافة (distance)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]

        # رسم المربع حول الوجه
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
        # كتابة الاسم فوق المربع
        cv2.rectangle(img, (left, bottom - 20), (right, bottom), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, name, (left + 2, bottom - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    # عرض الصورة في نافذة
    cv2.imshow("Face Recognition Result", img)
    print("[INFO] Press any key on the image window to close.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ------------------------------------------------------
# الدالة الرئيسية main()
# ------------------------------------------------------
if __name__ == "__main__":
    known_faces_dir = "known_faces"  # مجلد الوجوه المعروفة
    test_url = input("Enter image URL to recognize: ")

    recognize_faces_from_url(test_url, known_faces_dir)
