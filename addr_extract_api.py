from flask import Flask, jsonify
from flask_cors import CORS
from flask_sslify import SSLify

from webargs import fields, validate
from webargs.flaskparser import use_args, abort, parser
# from healthcheck import HealthCheck
import pyap
import json, os, traceback, hashlib
from google.cloud import storage
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./gcp_config.json"

# Initialise flask app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1600 * 1024 * 1024
CORS(app, supports_credentials=True)
sslify = SSLify(app)

# def create_folder(bucket_name, destination_folder_name):
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(destination_folder_name)

#     blob.upload_from_string('')

#     print('Created {} .'.format(
#         destination_folder_name))

def writeToGcs(url, htmlBlob):
    storage_client = storage.Client()
    try:
      now = datetime.now()
      # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
      bucket = storage_client.bucket('address-extractor-files')
      # folder = create_folder('address-extractor-files', f'{now}')
      filename = "{link}:-{time}.html".format(link = url, time = now)
      blob = bucket.blob(filename)

      blob.upload_from_string(
          data=json.dumps(htmlBlob),
          content_type='application/json'
      )
    except Exception:
      print('IN WRITE-TO-GCS')
      traceback.print_exc()
      pass

def getUrlId(url):
    try:
      hashStr = f'{url}'.encode('utf-8')
      urlId = hashlib.blake2b(hashStr, digest_size=6).hexdigest()
      return urlId
    except Exception:
        print("GET-URL-ID FUNCTION")
        traceback.print_exc()
        return None

@app.route("/extract", methods=["POST"])
@use_args(argmap={"textBlob": fields.Str(required=True, validate=[validate.Length(min=1, max=20000)]), "htmlBlob": fields.Str(required=True), "url": fields.Str(required=True)}, location="json")
def hello_from_body(args):
    """Method 3: Return hello with name, given in body"""
    text = args.get("textBlob", "")
    addresses = pyap.parse(text, country='US')
    addr = []
    for address in addresses:
      addr.append(str(address))
    html = args.get("htmlBlob", "")
    url = args.get("url", "")
    writeToGcs(url, html)
    urlId = getUrlId(url)
    return { "addresses": addr, "urlId": urlId }, 200

@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    abort(error_status_code, errors=err.messages)

if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=5000)
