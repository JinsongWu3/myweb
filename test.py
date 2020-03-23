from markdown import markdown
def m2h():
    f_paper_zh = open('static/source/paper_zh.txt', 'r')
    paper_zh = f_paper_zh.read()
    html_file = markdown(paper_zh, output_format = 'html')
    f_paper_zh.close()
    print(html_file)

# file_zh = open('static/source/patent_zh_src.txt', 'w', encoding='UTF-8')
#
# file_old = open('static/source/patent_zh_sq.txt', 'r', encoding='UTF-8')
# patent_zh = file_old.read()
# file_zh.write(patent_zh)
# file_zh.close()


r,c = list(map(int, input().split()))
m = [[None] for _ in range(r)]
dp = [1000000]*(c+1)
for i in range(r):
    m[i] = list(map(int, input().split()))

dp[c-1] = max(1, 1-m[r-1][c-1])
for i in range(c-2, -1, -1):
    dp[i] = max(1, dp[i+1]-m[r-1][i])
for i in range(r-2, -1,-1):
    for j in range(c-1, -1,-1):
        dp[j] = min(max(1, dp[j+1] - m[i][j]), max(1, dp[j]-m[i][j]))
print(dp[0])

print(dp)
