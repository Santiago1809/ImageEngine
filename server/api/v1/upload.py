from flask import Blueprint, request, jsonify
import os
from image.compress import comprimir_imagen

upload = Blueprint("upload", __name__)
directory = "c:/Users/Santiago/OneDrive/Escritorio/esrgan/server/api/images"


@upload.route("/api/v1/upload", methods=["POST"])
def upload_file():
    _file = request.files["file"]
    file_ext = os.path.splitext(_file.filename)[1]
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, _file.filename)
    _file.save(file_path)

    compressed_path = comprimir_imagen(file_path, file_ext)

    return jsonify(
        {
            "message": "File uploaded successfully",
            "file_path": file_path,
            "compressed_path": compressed_path,
        }
    )
