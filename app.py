from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return " Heramb Upadhye - 100919492 - ICE1"

if __name__ == "__main__":
    # Bind to 0.0.0.0 on port 8080 for Azure App Service (Linux containers)
    app.run(host="0.0.0.0", port=8080)


