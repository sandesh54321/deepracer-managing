from shared.shared import db, ma

class Participant( db.Model ):
    id = db.Column( db.Integer, primary_key=True )
    name = db.Column( db.String( 50 ))

    def __repr__( self ):
        return '<Participant %s>' % self.name

class ParticipantSchema( ma.Schema ):
    class Meta:
        fields = ( "id", "name" )