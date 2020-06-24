from flask_restful import Resource
from flask import request
from models.participant import Participant, ParticipantSchema
from shared.shared import db

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