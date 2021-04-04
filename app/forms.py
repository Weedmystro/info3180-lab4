from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired



class UploadForm(FlaskForm):
    photo=FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg','png', 'Images only!'])
    ])
    description = StringField('Description', validators=[DataRequired()])

    #picture = FileField('Picture', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])description = StringField('Description', validators=[DataRequired()])


