import os
import uuid
import re
from flask import current_app
import sys

def create_file(file):
    origin_filename = file.filename.encode('ascii', 'replace').decode('utf-8')
    origin_filename = file.filename
    file_id = str(uuid.uuid4())
    core_filename, file_type = os.path.splitext(origin_filename)
    filename = sys.path[0]+'/file/'+core_filename+file_type
    if not os.path.exists(filename):
        file.save(filename)
    return file_id
