import os
from flask import Flask
from routes.api_v1.endpoints.predict import predict
from routes.home import home
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
PORT = os.environ.get("PORT")
"""
Rota home default /
"""
app.register_blueprint(home)


"""
Rota /api/v1/predict
""" 
app.register_blueprint(predict, url_prefix="/api/v1/predict")


"""
Rota notFound
""" 
@app.errorhandler(404)
def page_not_found(error):
    return {'error': os.environ.get('NOTFOUND_REQUEST_MSG')}, 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT) 
