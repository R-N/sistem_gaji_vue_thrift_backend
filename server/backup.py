from flask import request, jsonify, send_from_directory, safe_join, abort
import json
from thrift.Thrift import TException

from models import get_model
from utils.request import get_args, json_error, get_file
from utils.file import last_modified

def download(download_token=''):
    args = {'download_token': download_token}
    args = get_args(request, args)
    download_token = args['download_token']
    ip = request.remote_addr
    model = get_model("backup")
    try:
        payload = model.decode_download_token(ip, download_token)
        return send_from_directory(model.backup_path, filename=payload['file_name'], as_attachment=True)
    except TException as err:
        return json_error(err)

def upload(upload_token=''):
    args = {'upload_token': upload_token}
    args = get_args(request, args)
    upload_token = args['upload_token']
    ip = request.remote_addr
    model = get_model("backup")
    try:
        payload = model.decode_upload_token(ip, upload_token)
        file = get_file(request, "file")
        file.filename = payload["file_name"]
        file.save(safe_join(model.backup_path, file.filename))
        print("Filename: " + file.filename)
        return {
            'file_name': file.filename,
            'last_modified': str(last_modified(safe_join(model.backup_path, file.filename)))
        }
    except TException as err:
        return json_error(err)

def init(app):
    app.route('/backup/download/<download_token>', methods=["GET"])(download)
    app.route('/backup/download/', methods=["POST", "GET"])(download)
    app.route('/backup/download', methods=["POST", "GET"])(download)
    app.route('/backup/upload/<upload_token>', methods=["POST"])(upload)
    app.route('/backup/upload/', methods=["POST"])(upload)
    app.route('/backup/upload', methods=["POST"])(upload)
