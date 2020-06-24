from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask( __name__ )
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "aws.db")
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'sqlite:///' + db_path
db = SQLAlchemy( app )
ma = Marshmallow( app )

api = Api( app )

class HelloWorld( Resource ):
    def get( self ):
        return { "hello": "world" }

class Participant( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 50 ))

    def __repr__( self ):
        return '<Participant %s>' % self.name

class ParticipantSchema( ma.Schema ):
    class Meta:
        fields = ( "id", "name" )

class ParticipantsResource(Resource):
    def get( self ):
        participants = Participant.query.all()
        return participants_schema.dump( participants )

    def post( self ):
        new_participant = Participant( name=request.json[ 'name' ] )
        db.session.add( new_participant )
        db.session.commit()
        return participant_schema.dump( new_participant )

participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema( many=True )

api.add_resource( ParticipantsResource, '/participants' )
api.add_resource( HelloWorld, '/' )

if __name__ == '__main__':
    app.run( debug=True )
