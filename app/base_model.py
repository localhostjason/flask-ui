from flask_sqlalchemy import Model


class BaseModel(Model):
    @staticmethod
    def enum_to_value(data):
        if not data:
            return None

        try:
            new_data = data.value
        except Exception:
            new_data = data
        return new_data

    @staticmethod
    def enum_to_name(data):
        if not data:
            return None
        try:
            new_data = data.name
        except Exception:
            new_data = data
        return new_data

    '''
    :param
      enum_type: show enum name or value
      extra_kw : extra property value
      extra_dict: extra dict 
      remove_key: del dict key
    @:return 
      return new dict
    '''

    def to_dict(self, enum_type='name', extra_kw=None, extra_dict=None, remove_key=list()):
        model_field = [v for v in self.__dict__.keys() if not v.startswith('_') and v not in remove_key]
        result = dict()
        for info in model_field:
            if enum_type == 'name':
                result[info] = self.enum_to_name(getattr(self, info))
            else:
                result[info] = self.enum_to_value(getattr(self, info))

        if extra_kw and isinstance(extra_kw, list):
            for info in extra_kw:
                if enum_type == 'name':
                    result[info] = self.enum_to_name(getattr(self, info))
                else:
                    result[info] = self.enum_to_value(getattr(self, info))

        if extra_dict and isinstance(extra_dict, dict):
            for k, v in extra_dict.items():
                result[k] = v

        return result
