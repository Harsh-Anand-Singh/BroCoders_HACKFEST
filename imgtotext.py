import sys
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


cols_names = ['Department', 'Semester', 'p1', 'p2', 'p3', 'p4', 'p5', 'Course']

course_data = pd.read_csv('course_preferences.csv',
                          header=None, names=cols_names)

feature_cols = ['Department', 'Semester', 'p1', 'p2', 'p3', 'p4', 'p5']

X = course_data[feature_cols]
X = X.values
Y = course_data.Course

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accurac…
                   [0:44 am, 09/04/2023] Harsh IIT: import cv2

                   import pytesseract

                   pytesseract.pytesseract.tesseract_cmd='C:/Program Files/Tesseract-OCR/tesseract.exe'


                   img=cv2.imread("GRADE.png")


                   gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


                   ret, thresh1=cv2.threshold(
                       gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)


                   rect_kernel=cv2.getStructuringElement(
                       cv2.MORPH_RECT, (18, 18))


                   dilation=cv2.dilate(thresh1, rect_kernel, iterations=1)


                   contours, hierarchy=cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                        cv2.CHAIN_APPROX_NONE)


                   im2=img.copy()


                   file=open("recognized.txt", "w+")
                   file.write("")
                   file.close()


                   for cnt in contours:
                   x, y, w, h=cv2.boundingRect(cnt)


                   rect=cv2.rectangle(
                       im2, (x, y), (x + w, y + h), (0, 255, 0), 2)


                   cropped=im2[y:y + h, x:x + w]


                   file=open("recognized.txt", "a")


                   text=pytesseract.image_to_string(cropped)


                   file.write(text)
                   file.write("\n")

                   # Close the file
                   file.close
