import os
from sklearn.svm import SVC
import joblib

X=[]
y=[]

for label in os.listdir("dataset"):
    folder = os.path.join("dataset", label)

    if not os.path.isdir(folder):
        continue

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        data = open(path).read().strip()

        values = list(map(float,data.split(",")))

        if len(values)==2:   # only accept correct samples
            X.append(values)
            y.append(label)

model=SVC()
model.fit(X,y)

os.makedirs("model",exist_ok=True)
joblib.dump(model,"model/gesture_model.pkl")

print("✅ Model trained successfully")
