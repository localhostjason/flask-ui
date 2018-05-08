# coding: utf8
import json


class JinjaEnv:
    def __init__(self):
        pass

    def init_app(self, app):
        app.jinja_env.add_extension('jinja2.ext.loopcontrols')
        app.jinja_env.filters["remove_none"] = self.remove_none
        app.jinja_env.filters["to_dict"] = self.to_dict
        app.jinja_env.filters["get_attr"] = self.get_attr
        app.jinja_env.filters["check_dict_is_null"] = self.check_dict_is_null
        app.jinja_env.filters["select_enum"] = self.select_enum

    @staticmethod
    def remove_none(l):
        new_list = [v for v in l if v]
        result = []
        for v in new_list:
            if isinstance(v, list):
                v = ','.join([info for info in v if info])
            result.append(v)
        return result

    @staticmethod
    def check_dict_is_null(data):
        if not data: return False
        for key, val in data.items():
            if val:
                return True
        return False

    @staticmethod
    def select_enum(data, name, value, format_key='name'):
        if not data: return []
        new_data = []
        for v in data:
            if format_key == 'name':
                if getattr(v, name).name == value:
                    new_data.append(v)
            if format_key == 'value':
                if getattr(v, name).value == value:
                    new_data.append(v)
        return new_data

    @staticmethod
    def get_attr(data, attr_key):
        if not data: return []
        r = [getattr(v, attr_key) for v in data if getattr(v, attr_key)]
        return r

    @staticmethod
    def check_json_format(raw_msg):
        """
        用于判断一个字符串是否符合Json格式
        :param self:
        :return:
        """
        if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
            try:
                json.loads(raw_msg, encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            return False

    def to_dict(self, json_data):
        if not json_data:
            return

        if not self.check_json_format(json_data):
            return

        result = json.loads(json_data)
        return result
