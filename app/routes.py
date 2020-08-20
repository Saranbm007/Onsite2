from flask import render_template, request
from PIL import Image
from io import BytesIO
import os

directory = r'D:\_Code\delta\Mentorship\onsite\onsite2\app\static\uploads\thumbnails'

from app.forms import ImageForm
from app import app

size = (200, 200)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ImageForm()
    if form.validate_on_submit():
        img = request.files['image']
        img.save(os.path.join(r'D:\_Code\delta\Mentorship\onsite\onsite2\app\static\uploads', img.filename))
        image = Image.open(img.stream)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(os.path.join(r'D:\_Code\delta\Mentorship\onsite\onsite2\app\static\uploads\thumbnails', img.filename))  
    thumbnail_names = []
    for f in os.listdir(directory):
        if f:
            thumbnail_names.append(f) 
    return render_template('index.html', form=form, thumbnail_names=thumbnail_names)

    