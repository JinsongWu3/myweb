from markdown import markdown
def m2h():
    f_paper_zh = open('static/source/paper_zh.txt', 'r')
    paper_zh = f_paper_zh.read()
    html_file = markdown(paper_zh, output_format = 'html')
    f_paper_zh.close()
    print(html_file)

file_zh = open('static/source/patent_zh_src.txt', 'w', encoding='UTF-8')

file_old = open('static/source/patent_zh_sq.txt', 'r', encoding='UTF-8')
patent_zh = file_old.read()
file_zh.write(patent_zh)
file_zh.close()
