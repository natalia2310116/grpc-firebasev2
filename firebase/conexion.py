import firebase_admin
from firebase_admin import credentials

def conexion():
    cred = credentials.Certificate("./grpc-firebase-firebase-adminsdk-3i2fn-17c58dded0.json")
    firebase_admin.initialize_app(cred)