from kea import *

class TomatoNovel(KeaTest):

    # @precondition(lambda self: d(text="听书").exists(retries=1, wait_time=0))
    # @rule()
    # def listen_novel_page(self):
    #     d(text="听书").click()
    #     assert d(text="推荐榜").exists() and d(text="小说").exists()

    @precondition(lambda self: d(text="书籍详情").exists(retries=1, wait_time=0))
    @rule()
    def novel_detail_page(self):
        d(text="书籍详情").click()
        assert d(text="书籍简介").exists()

    @precondition(lambda self: d(text="下载").exists(retries=1, wait_time=0))
    @rule()
    def download(self):
        d(text="下载").click()
        assert d(text="下载中").exists()

    # @precondition(lambda self: d(text="加入书架").exists(retries=1, wait_time=0))
    # @rule()
    # def add_novel(self):
    #     d(text="加入书架").click()
    #     assert d(text="已加书架").exists()

    @precondition(lambda self: d(text="已加书架").exists(retries=1, wait_time=0))
    @rule()
    def del_novel(self):
        d(text="已加书架").click()
        assert d(text="移出书架").exists()

# if __name__ == "__main__":
#     from hmdriver2.driver import Driver
#     d = Driver("4ABVB24930003947")
#     print(d(text="推荐").exists(retries=1, wait_time=0))
