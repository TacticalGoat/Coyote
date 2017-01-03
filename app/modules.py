from mongoengine import *

class Quote(Document):
	strike_price = StringField(required=True)
	call = EmbeddedDocumentField(Call)
	put = EmbeddedDocumentField(put)

class Option(Document):
	symbol = StringField(required=True)
	quotes = ListField(EmbeddedDocumentField(Quote))