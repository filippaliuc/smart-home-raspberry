import pyrebase
from firebaseConfig import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)


database = firebase.database()
storage = firebase.storage()
# storage_bucket = firebase.storage().bucket()


