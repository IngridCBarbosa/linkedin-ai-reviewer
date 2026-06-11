import firebase_admin

from firebase_admin import credentials


def initialize_firebase():

    cred = credentials.Certificate(
        "firebase-adminsdk.json"
    )

    firebase_admin.initialize_app(cred)

    print("Firebase initialized successfully")