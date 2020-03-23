from flask import render_template, Blueprint, request, flash, make_response,redirect,url_for, jsonify
from markdown import markdown
import os
import json
import rules
from flask import current_app
import sys

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
    file_zh = open('static/source/news_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en = open('static/source/news_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/news.html', content_en=content_en, content_zh=content_zh)

@Admin.route('/news_preview/', methods=['GET', 'POST'])
def news_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))

    file_zh = open('static/source/news_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_zh.close()
    file_en= open('static/source/news_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_en.close()
    content_zh = rules.text_news(content_zh, zh=True)
    content_en = rules.text_news(content_en, zh=False)
    content_zh = content_zh.split('\n')
    content_en = content_en.split('\n')
    return render_template('admin/news_preview.html', content_zh=content_zh, content_en=content_en)


@Admin.route('/paper/', methods=['GET', 'POST'])
def paper():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/paper_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en = open('static/source/paper_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/paper.html', content_zh=content_zh, content_en=content_en)

@Admin.route('/paper_preview/', methods=['GET', 'POST'])
def paper_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))

    file_zh = open('static/source/paper_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/paper_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    content_zh_thisyear,content_zh_before = rules.text_paper(content_zh, zh=True)
    content_en_thisyear,content_en_before = rules.text_paper(content_en, zh=False)
    # print(content_zh_thisyear)
    # print(content_zh_before)

    return render_template('admin/paper_preview.html',
                           content_zh_thisyear=content_zh_thisyear,
                           content_zh_before=content_zh_before,
                           content_en_thisyear=content_en_thisyear,
                           content_en_before=content_en_before,
                           )


@Admin.route('/competition/', methods=['GET', 'POST'])
def competition():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/competition_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en = open('static/source/competition_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/competition.html', content_en=content_en, content_zh=content_zh)

@Admin.route('/competition_preview/', methods=['GET', 'POST'])
def competition_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))

    file_zh = open('static/source/competition_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_zh.close()
    file_en = open('static/source/competition_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_en.close()
    content_zh = rules.text_competition(content_zh, zh=True).split('\n')
    content_en = rules.text_competition(content_en, zh=False).split('\n')

    return render_template('admin/competition_preview.html', content_zh=content_zh, content_en=content_en)


@Admin.route('/patent/', methods=['GET', 'POST'])
def patent():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    file_zh = open('static/source/patent_zh.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/patent_en.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    file_zh.close()
    file_en.close()
    return render_template('admin/patent.html',content_en=content_en, content_zh=content_zh)

@Admin.route('/patent_preview/', methods=['GET', 'POST'])
def patent_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    try:
        file_zh = open('static/source/patent_zh_src.txt', 'r', encoding='UTF-8')
        patent_zh = file_zh.read()
        file_zh.close()
        file_en= open('static/source/patent_en_src.txt', 'r', encoding='UTF-8')
        patent_en = file_en.read()
        file_en.close()
    except IOError as e:
        print(e)
    content_zh_zl, content_zh_sq = rules.text_patent(patent_zh, zh=True)
    content_en_zl, content_en_sq = rules.text_patent(patent_en, zh=False)
    content_zh_zl = content_zh_zl.split('\n')
    content_zh_sq = content_zh_sq.split('\n')
    content_en_zl = content_en_zl.split('\n')
    content_en_sq = content_en_sq.split('\n')


    return render_template('admin/patent_preview.html', content_zh_zl=content_zh_zl, content_zh_sq=content_zh_sq, content_en_zl=content_en_zl, content_en_sq=content_en_sq, mode='preview')


@Admin.route('/partner/', methods=['GET', 'POST'])
def partner():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    partners = os.listdir(r'static/partner/')

    try:
        file = open('static/source/partner_src.txt', 'r', encoding='UTF-8')
        content = file.read()
        file.close()
    except IOError as e:
        print(e)

    return render_template('admin/partner.html', partners=partners, content=content)


@Admin.route('/partner_preview/', methods=['GET', 'POST'])
def partner_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))

    try:
        file = open('static/source/partner_src.txt', 'r', encoding='UTF-8')
        partners = file.read().split('\n')
        file.close()
    except IOError as e:
        print(e)

    return render_template('admin/partner_preview.html', partners=partners)

@Admin.route('/pic/', methods=['GET', 'POST'])
def pic():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    pics = os.listdir(r'static/pic/')
    try:
        file = open('static/source/pic_src.txt', 'r', encoding='UTF-8')
        content = file.read()
        file.close()
    except IOError as e:
        print(e)
    return render_template('admin/pic.html', pics=pics, content=content)

@Admin.route('/pic_preview/', methods=['GET', 'POST'])
def pic_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    try:
        file = open('static/source/pic_src.txt', 'r', encoding='UTF-8')
        pics = file.read().split('\n')
        file.close()
        for i in range(len(pics)):
            pics[i] = pics[i].split('|')
    except IOError as e:
        print(e)
    return render_template('admin/pic_preview.html', pics=pics)


@Admin.route('/member/', methods=['GET', 'POST'])
def member():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    members = os.listdir(r'static/member/')
    try:
        file = open('static/source/member_src.txt', 'r', encoding='UTF-8')
        content = file.read()
        file.close()
    except IOError as e:
        print(e)
    return render_template('admin/member.html', members=members, content=content)

@Admin.route('/member_preview/', methods=['GET', 'POST'])
def member_preview():
    token = request.cookies.get('token')
    if token != admin_token:
        return redirect(url_for('.admin'))
    try:
        file = open('static/source/member_src.txt', 'r', encoding='UTF-8')
        members = file.read().split('\n')
        file.close()
        for i in range(len(members)):
            members[i] = members[i].split('|')
    except IOError as e:
        print(e)
    return render_template('admin/member_preview.html', members=members)





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


@Admin.route('/update_news/', methods=['POST'])
def update_news():
    content_zh = request.form.get('content_zh')
    content_en = request.form.get('content_en')
    content_zh.encode(encoding='UTF-8')
    content_en.encode(encoding='UTF-8')
    zh_list = content_zh.split('\n')
    en_list = content_en.split('\n')
    try:
        file_zh = open('static/source/news_zh_src.txt', 'w', encoding='UTF-8')
        file_en= open('static/source/news_en_src.txt', 'w', encoding='UTF-8')
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


@Admin.route('/update_competition/', methods=['POST'])
def update_competition():
    content_zh = request.form.get('content_zh')
    content_en = request.form.get('content_en')
    content_zh.encode(encoding='UTF-8')
    content_en.encode(encoding='UTF-8')
    zh_list = content_zh.split('\n')
    en_list = content_en.split('\n')
    try:
        file_zh = open('static/source/competition_zh_src.txt', 'w', encoding='UTF-8')
        file_en= open('static/source/competition_en_src.txt', 'w', encoding='UTF-8')
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

@Admin.route('/update_paper/', methods=['POST'])
def update_paper():
    content_zh = request.form.get('content_zh')
    content_en = request.form.get('content_en')
    content_zh.encode(encoding='UTF-8')
    content_en.encode(encoding='UTF-8')
    zh_list = content_zh.split('\n')
    en_list = content_en.split('\n')
    try:
        file_zh = open('static/source/paper_zh_src.txt', 'w', encoding='UTF-8')
        file_en= open('static/source/paper_en_src.txt', 'w', encoding='UTF-8')
        for i in zh_list:
            file_zh.writelines(i)
        for i in en_list:
            file_en.writelines(i)
        file_zh.close()
        file_en.close()
        res = json.dumps({'resultCode': 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/update_partner/', methods=['POST'])
def update_partner():
    content = request.form.get('content')
    content.encode(encoding='UTF-8')
    part_list = content.split('\n')
    try:
        file = open('static/source/partner_src.txt', 'w', encoding='UTF-8')
        for i in part_list:
            file.writelines(i)
        file.close()
        res = json.dumps({'resultCode': 200})
    except IOError as e:
        res = json.dumps({'resultCode': -1})
    return res

@Admin.route('/update_pic/', methods=['POST'])
def update_pic():
    content = request.form.get('content')
    content.encode(encoding='UTF-8')
    part_list = content.split('\n')
    try:
        file = open('static/source/pic_src.txt', 'w', encoding='UTF-8')
        for i in part_list:
            file.writelines(i)
        file.close()
        res = json.dumps({'resultCode': 200})
    except IOError as e:
        res = json.dumps({'resultCode': -1})
    return res

@Admin.route('/update_member/', methods=['POST'])
def update_member():
    content = request.form.get('content')
    content.encode(encoding='UTF-8')
    part_list = content.split('\n')
    try:
        file = open('static/source/member_src.txt', 'w', encoding='UTF-8')
        for i in part_list:
            file.writelines(i)
        file.close()
        res = json.dumps({'resultCode': 200})
    except IOError as e:
        res = json.dumps({'resultCode': -1})
    return res


@Admin.route('/pub_competition/')
def pub_competition():

    file_zh = open('static/source/competition_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/competition_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    content_zh = rules.text_competition(content_zh, zh=True)
    content_en = rules.text_competition(content_en, zh=False)
    file_zh.close()
    file_en.close()
    try:
        f_content_zh = open(current_app.config['COMPETITION_ZH'], 'w', encoding='UTF-8')
        f_content_en = open(current_app.config['COMPETITION_EN'], 'w', encoding='UTF-8')
        f_content_zh.write(content_zh)
        f_content_en.write(content_en)
        f_content_zh.close()
        f_content_en.close()
        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res


@Admin.route('/pub_news/')
def pub_news():

    file_zh = open('static/source/news_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/news_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    content_zh = rules.text_news(content_zh, zh=True)
    content_en = rules.text_news(content_en, zh=False)
    file_zh.close()
    file_en.close()
    try:
        f_content_zh = open(current_app.config['NEWS_ZH'], 'w', encoding='UTF-8')
        f_content_en = open(current_app.config['NEWS_EN'], 'w', encoding='UTF-8')
        f_content_zh.write(content_zh)
        f_content_en.write(content_en)
        f_content_zh.close()
        f_content_en.close()
        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/pub_paper/')
def pub_paper():

    file_zh = open('static/source/paper_zh_src.txt', 'r', encoding='UTF-8')
    content_zh = file_zh.read()
    file_en= open('static/source/paper_en_src.txt', 'r', encoding='UTF-8')
    content_en = file_en.read()
    content_zh = rules.text_competition(content_zh, zh=True)
    content_en = rules.text_competition(content_en, zh=False)
    file_zh.close()
    file_en.close()
    try:
        f_content_zh = open(current_app.config['PAPER_ZH'], 'w', encoding='UTF-8')
        f_content_en = open(current_app.config['PAPER_EN'], 'w', encoding='UTF-8')
        f_content_zh.write(content_zh)
        f_content_en.write(content_en)
        f_content_zh.close()
        f_content_en.close()
        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/pub_patent/')
def pub_patent():

    file_zh = open('static/source/patent_zh_src.txt', 'r', encoding='UTF-8')
    patent_zh = file_zh.read()
    #print(patent_zh)
    file_en= open('static/source/patent_en_src.txt', 'r', encoding='UTF-8')
    patent_en = file_en.read()
    patent_zh_zl, patent_zh_sq = rules.text_patent(patent_zh, zh=True)
    patent_en_zl, patent_en_sq = rules.text_patent(patent_en, zh=False)
    file_zh.close()
    file_en.close()
    try:
        f_patent_zh = open(current_app.config['PATENT_ZH'], 'w', encoding='UTF-8')
        f_patent_en = open(current_app.config['PATENT_EN'], 'w', encoding='UTF-8')

        f_patent_zh.write(patent_zh_zl)
        f_patent_zh.write('\n')
        f_patent_zh.write(patent_zh_sq)
        f_patent_en.write(patent_en_zl)
        f_patent_en.write('\n')
        f_patent_en.write(patent_en_sq)

        f_patent_zh.close()
        f_patent_zh.close()

        res = json.dumps({'resultCode' : 200})
        return res
    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/pub_partner/')
def pub_partner():
    try:
        file_src = open('static/source/partner_src.txt', 'r', encoding='UTF-8')
        partners = file_src.read()
        file_src.close()

        file = open('static/source/partner.txt', 'w', encoding='UTF-8')
        file.write(partners)
        res = json.dumps({'resultCode' : 200})
        return res

    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res


@Admin.route('/add_partner/', methods=['POST'])
def add_partner():

    img=request.files.get('img')
    img_path = sys.path[0]+'/static/partner/'+img.filename
    #print(img_path)
    partners = os.listdir('static/partner/')
    if img.filename not in partners:
        img.save(img_path)
        res = json.dumps({'resultCode': 200, 'img_path':img.filename})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/del_partner/', methods=['POST'])
def del_partner():
    img=request.form.get('filename')
    img_path = sys.path[0]+'/static/partner/'+img
    partners = os.listdir('static/partner/')
    if img  in partners:
        os.remove(img_path)
        res = json.dumps({'resultCode': 200})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/pub_pic/')
def pub_pic():
    try:
        file_src = open('static/source/pic_src.txt', 'r', encoding='UTF-8')
        partners = file_src.read()
        file_src.close()

        file = open('static/source/pic.txt', 'w', encoding='UTF-8')
        file.write(partners)
        res = json.dumps({'resultCode' : 200})
        return res

    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res


@Admin.route('/add_pic/', methods=['POST'])
def add_pic():

    img=request.files.get('img')
    img_path = sys.path[0]+'/static/pic/'+img.filename
    #print(img_path)
    partners = os.listdir('static/pic/')
    if img.filename not in partners:
        img.save(img_path)
        res = json.dumps({'resultCode': 200, 'img_path':img.filename})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/del_pic/', methods=['POST'])
def del_pic():
    img=request.form.get('filename')
    img_path = sys.path[0]+'/static/pic/'+img
    partners = os.listdir('static/pic/')
    if img  in partners:
        os.remove(img_path)
        res = json.dumps({'resultCode': 200})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res


@Admin.route('/pub_member/')
def pub_member():
    try:
        file_src = open('static/source/member_src.txt', 'r', encoding='UTF-8')
        partners = file_src.read()
        file_src.close()

        file = open('static/source/member.txt', 'w', encoding='UTF-8')
        file.write(partners)
        res = json.dumps({'resultCode' : 200})
        return res

    except IOError as e:
        res = json.dumps({'resultCode': -1})
        return res


@Admin.route('/add_member/', methods=['POST'])
def add_member():

    img=request.files.get('img')
    img_path = sys.path[0]+'/static/member/'+img.filename
    #print(img_path)
    partners = os.listdir('static/member/')
    if img.filename not in partners:
        img.save(img_path)
        res = json.dumps({'resultCode': 200, 'img_path':img.filename})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res

@Admin.route('/del_member/', methods=['POST'])
def del_member():
    img=request.form.get('filename')
    img_path = sys.path[0]+'/static/member/'+img
    partners = os.listdir('static/member/')
    if img  in partners:
        os.remove(img_path)
        res = json.dumps({'resultCode': 200})
        return res
    else:
        res = json.dumps({'resultCode': -1})
        return res
