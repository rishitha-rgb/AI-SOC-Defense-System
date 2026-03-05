import pickle

model = pickle.load(open("../ai_model/model.pkl","rb"))

def predict_attack(request):

    length = len(request)
    special = sum(not c.isalnum() for c in request)

    features = [[length,special]]

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "attack"
    else:
        return "normal"
