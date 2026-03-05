import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    "length":[20,25,200,300,40,35,250],
    "special_chars":[0,1,10,15,0,1,12],
    "label":[0,0,1,1,0,0,1]
}

df = pd.DataFrame(data)

X = df[["length","special_chars"]]
y = df["label"]

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model,open("model.pkl","wb"))

print("Model trained successfully")
