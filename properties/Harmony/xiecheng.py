from kea import *

class XieCheng(KeaTest):

    @precondition(lambda self: d(text="签证目的地").exists(retries=1, wait_time=0))
    @rule()
    def detail_page(self):
        d(text="签证目的地").click()
        assert d(text="热门").exists() and d(text="亚洲").exists() and d(text="取消").exists()