from haystack.signals import BaseSignalProcessor


class MyRealtimeSignalProcessor(BaseSignalProcessor):
    def handle_save(self, sender, instance, **kwargs):
        # 实现保存对象时的实时处理逻辑
        pass

    def handle_delete(self, sender, instance, **kwargs):
        # 实现删除对象时的实时处理逻辑
        pass
