# coding: utf8
import json


class JinjaEnv:
    def __init__(self):
        pass

    def init_app(self, app):
        app.jinja_env.add_extension('jinja2.ext.loopcontrols')
        app.jinja_env.filters["loads_jason"] = self.loads_jason

    @staticmethod
    def check_json_format(data):
        """
        用于判断一个字符串是否符合Json格式
        :param self:
        :return:
        """
        if not isinstance(data, str):
            return False

        try:
            json.loads(data)
        except ValueError:
            return False
        return True

    def loads_jason(self, json_data):
        if not json_data:
            return

        if not self.check_json_format(json_data):
            return

        result = json.loads(json_data)
        return result
