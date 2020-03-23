from flask import Flask, render_template, request, flash, Response,jsonify, send_from_directory,abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
import json
from file import create_file, remove_file
import os
import sys
from Admin import Admin
from config import config
import rules


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

@app.route('/patent/', methods=['GET'])
def patent():
    try:
        f_content = open(app.config['PATENT_ZH'], 'r', encoding='UTF-8')
        content = f_content.read()
        f_content.close()
        content_zl, content_sq = rules.text_patent(content)
        content_zl = content_zl.split('\n')
        content_sq = content_sq.split('\n')
    except IOError as e:
        return 'error'

    return render_template('patent.html', content_zl=content_zl, content_sq=content_sq, mode='view')

@app.route('/files', methods=['POST', 'DELETE'])
def handle_files():
    if request.method == 'POST':
        file = request.files['file']
        # validate assets type
        if file is None:
            return json.jumps({'code': -2, 'msg': 'Missing uploaded assets.'})
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
            return json.dumps({'code': -1, 'msg': 'Missing assets id.'})
        remove_file(file_id)
        return json.dumps({'code': 0, 'data': file_id})

@app.route('/static/paper/<filename>')
def download_file(filename):
    if os.path.isfile(os.path.join('static/paper/', filename)):
        return send_from_directory('static/paper/', filename, as_attachment=True)



@app.route('/test/')
def test():
    picdata=[]
    pic1 = {'ID': 1, 'path': 'static/1.jpg'}
    pic2 = {'ID': 2, 'path': 'static/2.jpg'}
    picdata.append(pic1)
    picdata.append(pic2)
    return render_template('test.html', picdata=picdata)

if __name__ == '__main__':
    app.run(debug=True)
