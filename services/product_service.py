"""from firebase_admin import firestore"""
from firebase_admin import firestore


def get_all_product():
    db = firestore.client()
    docs = db.collection("productos").stream()

    for doc in docs:
        print(f"{doc.id}=> {doc.to_dict()}")