import url_manager, html_downloader, html_parser, html_outputer

class SpiderMain(object):
  def __init__(self):  # 初始化
    self.urls = url_manager.UrlManager()   # url管理器
    self.downloader = html_downloader.HtmlDownloader()  # 下载器
    self.parser = html_parser.HtmlParser()   # 解析器
    self.outputer = html_outputer.HtmlOutputer()  # 输出器

  def craw(self, root_url):
    count = 1

    # 添加新的url地址
    self.urls.add_new_url(root_url)

    # 遍历所有url列表
    while self.urls.has_new_url():
      try:
        new_url = self.urls.get_new_url()        # 获取url
        print('craw %d : %s' % (count, new_url))    
        html_cont = self.downloader.download(new_url)    # 获取url对应的页面内容
        new_urls, new_data = self.parser.parse(new_url, html_cont)   # 获取页面上href列表以及标题，介绍信息
        self.urls.add_new_urls(new_urls)       # 添加新的url列表到列表中
        self.outputer.collect_data(new_data)     # 收集标题，介绍数据
      
        if count == 1000:    # 获取1000条数据暂停
          break
    
        count = count + 1
      
      except Exception as e:
        print('craw_failed', str(e))     

    self.outputer.output_html()       # 生成html页面

# 当模块被直接运行则开始爬虫
if __name__=="__main__":
  root_url = "https://baike.baidu.com/item/Python/407313"
  obj_spider = SpiderMain()
  obj_spider.craw(root_url)