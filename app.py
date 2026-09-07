from flask import Flask 

app = Flask(__name__)

@app.route("/")
def home():
	return {"Message": "Deveops project running"}

@app.route("/health")
def health():
	return {"status": "Ok"}

if __name__ == "__main__":
	app.run(debug=True)

