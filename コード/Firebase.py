import firebase_admin
from firebase_admin import credentials, firestore

cred =credentials.Certificate('./<your_service _account _json_file_path>')
app = firebase_admin.initialize_app(cred)

db = firestore.client()

# firebaseに新規データを格納
new_ref = db.collection('<your_collection>').document('<your_document>')
new_data = {
    '<field>': '<data>'
}
new_ref.set(new_data)

# firebaseからデータ取り出し
ref = db.collection('<your_collection>')
docs = ref.get()
for doc in docs:
    data = doc.to_dict()
    print('{}'.format(data['<field>']))