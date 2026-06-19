from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import pandas as pd

data = {
    "keywords":[
        "bank transaction account money",
        "bitcoin crypto wallet blockchain",
        "social media facebook instagram",
        "passport identity legal document",
        "family photos memories",
        "tax income return bank",
        "linkedin professional profile",
        "property ownership agreement legal"
    ],

    "category":[
        "Financial",
        "Financial",
        "Social",
        "Legal",
        "Personal",
        "Financial",
        "Social",
        "Legal"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["keywords"])

y = df["category"]

model = SVC(probability=True)

model.fit(X, y)

def classify_asset(text):

    test = vectorizer.transform([text])

    prediction = model.predict(test)[0]

    confidence = round(
        max(model.predict_proba(test)[0]) * 100,
        2
    )

    return prediction, confidence