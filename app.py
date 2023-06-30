from flask import Flask
from flask_restful import Api
from resources.base import Dados, processo


app = Flask(__name__)
api = Api(app)
    
api.add_resource(Dados, '/dados')
api.add_resource(processo, '/dados/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000/dados