from flask import Blueprint, render_template, request, redirect, current_app, Flask
from flask_login import login_required, current_user

import os

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

# current_app.config["FILE_UPLOADS"] = r"app\website\static\uploads"


@views.route('/upload', methods=["GET", "POST"])
@login_required
def upload():

    if request.method=="POST":
        if request.files:
            file = request.files["dataset"]
            print(file)
            # file.save(os.path.join(current_app.config["FILE_UPLOADS"], file.filename))
            # file.save(os.path.join('static/uploads', file.filename))

            print("image saved")
            return redirect(request.url)

    return render_template("upload.html", user=current_user)