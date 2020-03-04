import re


patent_re_zh={r'##.*##':' [[详情]](http://'}
patent_re_en={r'##.*##':' [[details]](http://'}

# 返回专利号和申请号
def text_patent(src, zh=True):
    ZL, SQ='', ''

    #中英文切换
    patent_re = patent_re_zh if zh else patent_re_en
    judge_word = '专利号' if zh else "patent number"

    content = src.split('\n')
    for row in content:
        if len(row)==0:
            continue
        for p in patent_re.keys():
            ans = re.search(p, row)
            if ans:
                l, r = ans.span()
                key_word = row[l+2:r-2]
                trans_word = patent_re[p]+key_word+')'
                row = row[:l]+trans_word+row[r:]
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



if __name__ == "__main__":
    fd = open('input.txt',encoding='UTF-8')
    text = fd.read()
    zl, sq = text_patent(src=text, zh=True)
    print('已授权:')
    print(zl)
    print('已受理:')
    print(sq)
