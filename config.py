import os
class Config: ##config子类
    DEBUG = False
    TESTING = False
    paper_zh = 'static/source/paper_zh.txt'
    paper_en ='static/source/paper_en.txt'
    news_en = 'static/source/news_en.txt'
    competition_en = 'static/source/competition_zh.txt'
    competition_zh = 'static/source/competition_en.txt'
    PATENT_ZH = 'static/source/patent_zh.txt'
    PATENT_EN = 'static/source/patent_en.txt'
    NEWS_ZH = 'static/source/news_zh.txt'
    NEWS_EN = 'static/source/news_en.txt'
    COMPETITION_ZH = 'static/source/competition_zh.txt'
    COMPETITION_EN = 'static/source/competition_en.txt'
    PAPER_ZH = 'static/source/paper_zh.txt'
    PAPER_EN = 'static/source/paper_en.txt'

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):#继承config基类
# 实际使用的config模块
  MY_KEY = 'This is my key'

class DevelopmentConfig(Config):
##开发人员使用的Config
  DEBUG = True
  MY_KEY = 'This is my key'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
