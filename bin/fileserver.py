from flask import Flask, redirect, request
import os

app = Flask(__name__)

TEMPLATE = """
<html>
<body>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="upload" />
<input type="submit" />
</form>
</body>
</html>
"""
UPLOADS = "uploads"

try:
    os.makedirs(UPLOADS)
except FileExistsError:
    pass


@app.route("/", methods=["GET"])
def form():
    return TEMPLATE


@app.route("/", methods=["POST"])
def receive_file():
    if "upload" not in request.files:
        print("No 'upload' in request.files")
        return redirect(request.url)
    upload = request.files["upload"]
    upload.save(os.path.join(UPLOADS, upload.filename))
    return redirect(request.url)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
