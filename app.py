from flask import Flask, render_template, request, flash, Response,jsonify, send_from_directory,abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json
from file import create_file
import os
import sys
from Admin import Admin
from config import config


app = Flask(__name__)
app.config.from_object(config['development'])
config['development'].init_app(app)


app.register_blueprint(Admin, url_prefix='/admin')
app.secret_key='sdfsfadf'


class mrForm(FlaskForm):
    username = SubmitField()
    password = PasswordField()
    submit = SubmitField()


'''@app.route('/admin',methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        token = request.form.get('token')
        if token == admin_token:

            return render_template('edit.html')
        flash(u'验证错误')

    return render_template('admin.html')
    '''

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('edit.html')

@app.route('/files', methods=['POST', 'DELETE'])
def handle_files():
    if request.method == 'POST':
        file = request.files['file']
        # validate file type
        if file is None:
            return json.jumps({'code': -2, 'msg': 'Missing uploaded file.'})
        try:
            file_id = create_file(file)
            print('ok')
            return json.dumps({'code': 0, 'data': file_id})
        except ValueError as e:
            print(str(e))
            return json.dumps({'code': -1, 'msg': str(e)})
    else:
        file_id = request.data.decode('utf-8')
        if file_id is None or file_id == '':
            return json.dumps({'code': -1, 'msg': 'Missing file id.'})
        #remove_file(file_id)
        return json.dumps({'code': 0, 'data': file_id})

@app.route('/file/<filename>')
def download_file(filename):
    if os.path.isfile(os.path.join('file', filename)):
        return send_from_directory('file', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
