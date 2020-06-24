from flask import Flask
from flask_restful import Resource, Api
from shared.shared import db, ma
import os
from controllers.participants import ParticipantsResource

app = Flask( __name__ )
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "aws.db")
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///' + db_path
db.init_app( app )
ma.init_app( app )

api = Api( app )

class HelloWorld( Resource ):
    def get( self ):
        return { "hello": "world" }

api.add_resource( ParticipantsResource, '/participants' )
api.add_resource( HelloWorld, '/' )

if __name__ == '__main__':
    app.run( debug=True )
