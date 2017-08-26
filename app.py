"""Dropbox Public Folder Proxy App."""
import dropbox
import dropbox.files
import requests

from config import access_token
from flask import Flask, Response, stream_with_context, abort


dbx = dropbox.Dropbox(access_token)


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    """Page Not Found Response."""
    return "File Not found"


@app.route("/<path:file_path>")
def index(file_path):
    """Homepage."""
    try:
        public_file = dbx.files_get_temporary_link('/Public/{}'.format(file_path))
    except:
        abort(404)

    # Stream public file to browser.
    public_file_url = public_file.link
    req = requests.get(public_file_url, stream=True)
    return Response(
        stream_with_context(req.iter_content()),
        content_type=req.headers['content-type'])
