from mongoengine import Document, fields


class FrequencyTable(Document):
    query = fields.StringField(max_length=100, null=False, unique=True)
    frequency = fields.IntField(null=False)

    meta = {
        'ordering': ['frequency'],
        'collection': 'search_frequencytable'
    }
