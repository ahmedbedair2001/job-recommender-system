from flask import Flask,request,jsonify
from flask_cors import CORS
import Recommender

app = Flask(__name__)
CORS(app) 
        
@app.route('/job', methods=['GET'])
def recommend_jobs():
        res = Recommender.results(request.args.get('title'))
        return jsonify(res)

if __name__=='__main__':
        app.run(port = 5000, debug = True)