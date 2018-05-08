# -*- coding: utf-8 -*-
from flask import flash, redirect, request, current_app
import json
from wtforms import SelectMultipleField
from wtforms import widgets
import time


def pagination_result(model, new_per_page=None):
    page = request.args.get('page', 1, type=int)
    per_page = current_app.config['FLASKY_PER_PAGE'] if not new_per_page else new_per_page

    pagination = model.paginate(page, per_page=per_page, error_out=False)
    return pagination


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class Check:
    __slots__ = [
        'form',
    ]

    def __init__(self, form):
        self.form = form

    '''
        message type in ['errors', 'warning', 'success', 'info']
    '''

    def check_validate_on_submit(self, message_type='errors'):
        if request.method == 'POST':
            if not self.form.validate_on_submit():
                print(self.form.errors)
                for key, val in self.form.errors.items():
                    if '不是有效的整数' in val:
                        val.remove('不是有效的整数')
                    if '不是有效的浮点数' in val:
                        val.remove('不是有效的浮点数')
                flash({message_type: self.form.errors})
                return redirect(request.url)

    @staticmethod
    def update_model(model, data):
        if not data:
            return False

        if isinstance(data, dict):
            for k, v in data.items():
                setattr(model, k, v)


class BaseForm:
    def __init__(self):
        pass

    def get_field(self):
        field = [v for v in self.__dict__.keys() if not v.startswith('_') and
                 v not in ['meta', 'csrf_token', 'submit']]
        return field

    def required_form(self, **kwargs):
        field = self.get_field()
        for v in field:
            if getattr(self, v).flags.required:
                required_field = {'required': True}
                new_kwargs = kwargs.get(v) or dict()
                getattr(self, v).render_kw = dict(required_field, **new_kwargs)

    def get_form_data(self):
        field = self.get_field()
        result = dict()
        for field_info in field:
            field_data = getattr(self, field_info).data
            if field_data:
                if isinstance(field_data, list):
                    result[field_info] = ','.join(field_data)
                else:
                    result[field_info] = field_data
        return result

    @staticmethod
    def is_json(obj):
        if isinstance(obj, str):
            try:
                json.loads(obj, encoding='utf-8')
            except ValueError:
                return False
            return True
        else:
            return False

    def set_form_data(self, obj, form_keys=None, split_key=None):
        if not obj:
            return

        form_keys = form_keys or self.get_field()

        if not isinstance(form_keys, list):
            raise AttributeError('form_keys is not list')

        for info in form_keys:
            if isinstance(obj, dict):
                getattr(self, info).data = obj.get(info) or ''
            else:
                if info in obj.__dict__.keys() and getattr(obj, info):
                    getattr(self, info).data = getattr(obj, info)

        if split_key:
            for sk in split_key:
                getattr(self, sk).data = (getattr(obj, sk) or '').split(',')

    @staticmethod
    def update_model(query, params):
        if not params:
            return False

        for col, val in params.items():
            setattr(query, col, val)


class Tool:
    def __init__(self):
        pass

    @staticmethod
    def time_to_date(localtime):
        try:
            int_time = int(localtime)
        except Exception as e:
            print(e)
            return

        t = time.localtime(int_time)
        format_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        return format_time
