from kea import *

class Wechat(KeaTest):

    @precondition(lambda self: d(text="个人名片").exists(retries=1, wait_time=0))
    @rule()
    def forward_namecard(self):
        d(text="个人名片").long_click()
        assert d(text="转发").exists()
        d.click(text="转发")
        assert d(text="创建聊天").exists()

    @precondition(lambda self: d(text="撤回").exists(retries=1, wait_time=0))
    @rule()
    def revert(self):
        d(text="撤回").long_click()
        assert d(text="你撤回了一条消息 重新编辑").exists() or d(text="你撤回了一条消息").exists()