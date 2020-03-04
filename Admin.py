from flask import render_template, Blueprint, request, flash, make_response,redirect,url_for
from markdown import markdown
import json
import rules
from flask import current_app

Admin = Blueprint('admin', __name__, url_prefix="/admin")
admin_token = 'ubuntu'
txtfile_dic = {'paper_zh': 'static/source/paper_zh.txt',
               'paper_en': 'static/source/paper_en.txt',
               'news_zh': 'static/source/news_zh.txt',
               'news_en': 'static/source/news_en.txt',
               'competition_en': 'static/source/competition_zh.txt',
               'competition_zh': 'static/source/competition_en.txt',
               'patent_zh': 'static/source/patent_zh_sq.txt',
               'patent_en': 'static/source/patent_en_sq.txt',
               }

@Admin.route('/', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        token = request.form.get('token')
        print(token)
        if token == admin_token:
            f_paper_zh = open('static/source/paper_zh.txt', 'r', encoding='UTF-8')
            paper_zh = f_paper_zh.read()
            f_paper_en = open('static/source/paper_en.txt', 'r', encoding='UTF-8')
            paper_en = f_paper_en.read()
            f_paper_zh.close()
            f_paper_en.close()
            resp = make_response(render_template('admin/paper.html', paper_zh=paper_zh, paper_en=paper_en))
            resp.set_cookie('token', token)
            return resp
        flash('error')
    return render_template('admin.html')


@Admin.route('/news/', methods=['GET', 'POST'])
def news():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/news_zh.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en = open('static/source/news_en.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/news.html', content_en=content_en, content_zh=content_zh)


@Admin.route('/pic/', methods=['GET', 'POST'])
def pic():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    return render_template('admin/pic.html')


@Admin.route('/paper/', methods=['GET', 'POST'])
def paper():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    f_paper_zh = open('static/source/paper_zh.txt', 'r', encoding='UTF-8')
    paper_zh = f_paper_zh.read()
    f_paper_en = open('static/source/paper_en.txt', 'r', encoding='UTF-8')
    paper_en = f_paper_en.read()
    f_paper_zh.close()
    f_paper_en.close()
    return render_template('admin/paper.html', paper_zh=paper_zh, paper_en=paper_en)



@Admin.route('/competition/', methods=['GET', 'POST'])
def competition():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/competition_zh.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en = open('static/source/competition_en.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/competition.html', content_en=content_en, content_zh=content_zh)


@Admin.route('/member/', methods=['GET', 'POST'])
def member():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    return render_template('admin/member.html')


@Admin.route('/patent/', methods=['GET', 'POST'])
def patent():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/patent_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/patent_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/patent.html',content_en=content_en, content_zh=content_zh)

@Admin.route('/patent_preview/', methods=['GET', 'POST'])
def patent_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))

    file_zh = open('static/source/patent_zh_src.txt', 'r', encoding='UTF-8')
    patent_zh = file_zh.read()
    file_en= open('static/source/patent_en_src.txt', 'r', encoding='UTF-8')
    patent_en = file_en.read()
    patent_zh_zl, patent_zh_sq = rules.text_patent(patent_zh, zh=True)
    patent_en_zl, patent_en_sq = rules.text_patent(patent_en, zh=False)
    #patent_zh_zl = markdown(patent_zh_zl, output_format = 'html')
    #patent_zh_sq = markdown(patent_zh_sq, output_format = 'html')

    return render_template('admin/patent_preview.html', patent_zh_zl=patent_zh_zl, patent_zh_sq=patent_zh_sq, patent_en_zl=patent_en_zl, patent_en_sq=patent_en_sq)


@Admin.route('/partner/', methods=['GET', 'POST'])
def partner():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    return render_template('admin/partner.html')


@Admin.route('/upload_file/', methods=['GET', 'POST'])
def upload_file():
    print("upup")


#处理所有的txt文件
@Admin.route('/pub/<filename>/', methods=['POST'])
def pub_txtfile(filename):
    if filename not in txtfile_dic:
        return 'error'
    #print(filename, txtfile_dic[filename])
    content = request.form.get(filename)
    try:
        fd = open(txtfile_dic[filename], 'w', encoding='UTF-8')
        fd.write(content)
        fd.close()
        res = json.dumps({'resultCode': 200})
        return res
    except IOError as e:
        print(e)
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/update_patent/', methods=['POST'])
def update_patent():
    content_zh = request.form.get('content_zh')
    content_en = request.form.get('content_en')
    content_zh.encode(encoding='UTF-8')
    content_en.encode(encoding='UTF-8')
    zh_list=content_zh.split('\n')
    en_list=content_en.split('\n')
    try:
        file_zh = open('static/source/patent_zh_src.txt', 'w', encoding='UTF-8')
        file_en= open('static/source/patent_en_src.txt', 'w', encoding='UTF-8')
        for i in zh_list:
            file_zh.writelines(i)
        for i in en_list:
            file_en.writelines(i)
        file_zh.close()
        file_en.close()
        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res






@Admin.route('/pub_patent/')
def pub_patent():

    file_zh = open('static/source/patent_zh_src.txt', 'r', encoding='UTF-8')
    patent_zh = file_zh.read()
    print(patent_zh)
    file_en= open('static/source/patent_en_src.txt', 'r', encoding='UTF-8')
    patent_en = file_en.read()
    patent_zh_zl, patent_zh_sq = rules.text_patent(patent_zh, zh=True)
    patent_en_zl, patent_en_sq = rules.text_patent(patent_en, zh=False)
    file_zh.close()
    file_en.close()
    try:
        f_patent_zh_zl = open(current_app.config['PATENT_ZH_ZL'], 'w', encoding='UTF-8')
        f_patent_zh_sq = open(current_app.config['PATENT_ZH_SQ'], 'w', encoding='UTF-8')
        f_patent_en_zl = open(current_app.config['PATENT_EN_ZL'], 'w', encoding='UTF-8')
        f_patent_en_sq = open(current_app.config['PATENT_EN_SQ'], 'w', encoding='UTF-8')

        f_patent_zh_zl.write(patent_zh_zl)
        f_patent_zh_sq.write(patent_zh_sq)
        f_patent_en_zl.write(patent_en_zl)
        f_patent_en_sq.write(patent_en_sq)

        f_patent_zh_zl.close()
        f_patent_zh_sq.close()
        f_patent_en_zl.close()
        f_patent_en_sq.close()

        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res

