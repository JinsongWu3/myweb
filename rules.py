import re



paper_re_zh = {r'##(.*)##': r' <a href = "/static/paper/\g<1>">[论文]</a>',
               '\$\$(.*)\$\$':r' <a href = "/static/paper/\g<1>">[视频]</a>',
               r'@@(.*)@@': r' <a href = "/static/paper/\g<1>">[海报]</a>',
               r'&&(.*)&&': r' <a href = "/static/paper/\g<1>">[数据集]</a>'}
paper_re_en = {r'##(.*)##':  r' <a href = "/static/paper/\g<1>">[paper]</a>',
               '\$\$(.*)\$\$': r' <a href = "/static/paper/\g<1>">[video]</a>',
               r'@@(.*)@@': r' <a href = "/static/paper/\g<1>">[poster]</a>',
               r'&&(.*)&&': r' <a href = "/static/paper/\g<1>">[dataset]</a>'}

news_re_zh = {r'##(.*)##': r' <a href = "https://\g<1>">[详情]</a>'}
news_re_en = {r'##(.*)##': r' <a href = "https://\g<1>">[details]</a>'}

patent_re_zh = {r'##(.*)##': r' <a href = "https://\g<1>">[详情]</a>'}
patent_re_en = {r'##(.*)##': r' <a href = "https://\g<1>">[details]</a>'}

competiton_re_zh = {r'##(.*)##': r' <a href = "https://\g<1>">[详情]</a>'}
competiton_re_en = {r'##(.*)##': r' <a href = "https://\g<1>">[details]</a>'}


# 返回专利号和申请号


def text_competition(src, zh=True):
    competiton_re = competiton_re_zh if zh else competiton_re_en
    for p in competiton_re.keys():
        src = re.sub(p, competiton_re[p], src)
    return src

def text_news(src, zh=True):
    news_re = news_re_zh if zh else news_re_en
    for p in news_re.keys():
        src = re.sub(p, news_re[p], src)
    return src

def text_paper(src, zh=True):
    paper_re = paper_re_zh if zh else paper_re_en
    for p in paper_re.keys():
        src = re.sub(p, paper_re[p], src)
    src_thisyear, src_before = [], []
    src = src.split('\n')
    cnt = 0
    for i in src:
        i = i.strip()
        if len(i) < 16:
            cnt += 1
        if cnt <= 1:
            paper_i = i.split('|')
            src_thisyear.append(paper_i)
        else:
            src_before.append(i)
    return src_thisyear, src_before


def text_patent(src, zh=True):
    ZL, SQ='', ''

    #中英文切换
    patent_re = patent_re_zh if zh else patent_re_en
    judge_word = '专利号' if zh else "Patent No"

    # 正则替换
    for p in patent_re.keys():
        src = re.sub(p, patent_re[p], src)
    # 专利分类
    # ZL:专利号  SQ：申请号
    content = src.split('\n')
    for row in content:
        if len(row) == 0:
            continue
        row+='\n'
        if re.search(judge_word, row):
            ZL+=row
        else:
            SQ+=row
    if not ZL:
        ZL += '\n'
    if not SQ:
        SQ += '\n'
    return ZL[:-1], SQ[:-1]


# test
if __name__ == "__main__":
    fd = open('input.txt',encoding='UTF-8')
    text = fd.read()
    zl, sq = text_patent(src=text, zh=True)
    print('已授权:')
    print(zl)
    print('已受理:')
    print(sq)
