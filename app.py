from flask import(
    Flask,
    jsonify,
    request
    )
import pickle
import numpy as np

model = None
def create_app(test_config = None):
    app = Flask(__name__)
    model =  pickle.load(open('Decision_tree_model.pkl', 'rb'))
    @app.route('/')
    def welcome():
        print('Hello AI rate')
        return 'Hello AI rate'
        
    @app.route('/rate', methods=['POST'])
    def rate():
        x = request.json['data']
        print(x)
        x = [x]
        #print(x)
        pred = predict(x)
        return jsonify({
            'rate' : pred[0]
            })
#AI Module
    def predict(x):
        prediction = model.predict(x)
        return prediction
    
    return app
APP = create_app()

if __name__=='__main__':
    APP.run()
    #APP.run(host='0.0.0.0', port = 5000, debug = False)
    #APP.run(debug=True)