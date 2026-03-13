from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>This is Sunil who is working hard on DevOps</h2>
    <h3>Loves Gayathri</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


