import pyrebase
from firebaseConfig import firebaseConfig

# Inițializarea configurației Firebase utilizând firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)

# Obținerea referinței către baza de date
database = firebase.database()

# Obținerea referinței către stocarea de fișiere
storage = firebase.storage()

