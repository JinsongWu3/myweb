import os
class Config: ##config子类
    DEBUG = False
    TESTING = False
    paper_zh = 'static/source/paper_zh.txt'
    paper_en ='static/source/paper_en.txt'
    news_en = 'static/source/news_en.txt'
    competition_en = 'static/source/competition_zh.txt'
    competition_zh = 'static/source/competition_en.txt'
    PATENT_ZH_ZL = 'static/source/patent_zh_zl.txt'
    PATENT_ZH_SQ = 'static/source/patent_zh_sq.txt'
    PATENT_EN_ZL = 'static/source/patent_en_zl.txt'
    PATENT_EN_SQ = 'static/source/patent_en_sq.txt'

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
