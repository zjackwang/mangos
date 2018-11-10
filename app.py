from flask import Flask
from models import db

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, World!'

# App config
if __name__ = '__main__':
    app.config['DEBUG'] = True
    db.init_app(app)
    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'my_database',
        'host': 'localhost',
        'port': '5432',
    }
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' \
        % POSTGRES



    
    app.run()

