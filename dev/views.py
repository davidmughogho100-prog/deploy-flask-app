import os
import io
import tabula
import pandas as pd
from fileinput import filename
from flask import Blueprint, render_template, request, send_file, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
view = Blueprint("view", __name__, template_folder="templates")

@view.route("/", methods=["GET", "POST"])
@login_required
def home_page():
    if request.method == "POST":
        if "user_file" not in request.files:
            return "No file part", 400

        file = request.files["user_file"]
        if file.filename == "":
            return "No selected file", 400

        # file rename
        base_filename = os.path.splitext(file.filename)[0]
        new_filename = f"{base_filename}.csv"

        #---------------------------------------------------
        # file processing
        try:
            df_list = tabula.read_pdf(file.stream, pages="all", multiple_tables=True)
            if not df_list:
                return "No tables found in the pdf", 400

            # combine all the dataframes
            df_combined = pd.concat(df_list, ignore_index=True)
            # write to csv in memory

            csv_output = io.BytesIO()
            df_combined.to_csv(csv_output, index=False, encoding="utf-8")
            csv_output.seek(0)

            # return the processed data back to the user
            return send_file(csv_output, as_attachment=True, download_name=new_filename, mimetype="text/to_csv")

        except Exception as e:
            return f"An error occured", 500

        #------------------------------------------------------------
    return render_template("index.html") 

@view.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("view.home_page"))







