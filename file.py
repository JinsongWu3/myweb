import os
import uuid
import re
from flask import current_app
import sys

def create_file(file):
    origin_filename = file.filename.encode('ascii', 'replace').decode('utf-8')
    #origin_filename = file.filename
    core_filename, file_type = os.path.splitext(origin_filename)
    filename = sys.path[0]+'/static/paper/'+core_filename+file_type
    if not os.path.exists(filename):
        file.save(filename)
    return origin_filename

def remove_file(file_name):

    filename = sys.path[0]+'/static/paper/'+file_name
    if not os.path.exists(filename):
        return
    else:
        os.remove(filename)

