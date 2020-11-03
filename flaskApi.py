from flask import Flask
from election import apiInfo
app = Flask(__name__)
#prevent flask from sorting dictionary keys by default
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def returnAllInfo():
	return apiInfo

if __name__ == "__main__":
  app.run()