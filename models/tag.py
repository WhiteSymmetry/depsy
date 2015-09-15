from app import db
from sqlalchemy.dialects.postgresql import JSONB




class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Text, primary_key=True)
    name = db.Column(db.Text)
    namespace = db.Column(db.Text)
    count = db.Column(db.Integer)



    def __repr__(self):
        return u'<Tag "{}">'.format(self.id)

    @property
    def as_search_result(self):
        ret = {
            "name": self.name,
            "namespace": self.namespace,
            "type": "Tag",
            "sort_score": self.count,
            "summary": None
        }
        return ret
