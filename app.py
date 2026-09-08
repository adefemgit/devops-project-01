from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
	return {"Message": "Deveops project running"}

@app.route("/health")
def health():
	return {"status": "Ok"}

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False)

