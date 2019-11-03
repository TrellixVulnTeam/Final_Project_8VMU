from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    # title = StringField('Title', [validators.Length(min=0, max=30)])
    # category = StringField('Category', [validators.Length(min=0, max=30)])
    # text = TextAreaField('Text', [validators.Length(min=0, max=500)])

    lifetime = StringField('Lifetime', [validators.Length(min=1, max=30)])
    employment = StringField('Employment', [validators.Length(min=1, max=30)])
    income = StringField('Income', [validators.Length(min=1, max=30)])
    premium = StringField('Premium', [validators.Length(min=1, max=30)])
    lastclaim = StringField('Lastclaim', [validators.Length(min=1, max=30)])
    inception = StringField('Inception', [validators.Length(min=1, max=30)])
    claimamount = StringField('Claimamount', [validators.Length(min=1, max=30)])
    	
	#text = TextAreaField('Text', [validators.Length(min=0, max=500)])