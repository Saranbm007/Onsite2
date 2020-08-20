from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import ValidationError, DataRequired

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

class ImageForm(FlaskForm):
    image = FileField('Image', validators=[DataRequired()])
    submit = SubmitField('Upload')

    def validate_image(self, image):
        if not ('.' in image.data.filename and \
         image.data.filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS):
            raise ValidationError('Image type not valid')