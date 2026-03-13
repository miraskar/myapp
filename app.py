from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "This is Sunil who is working hard on Devops/n Loves Gayathri"

app.run(host='0.0.0.0',port=5000)
