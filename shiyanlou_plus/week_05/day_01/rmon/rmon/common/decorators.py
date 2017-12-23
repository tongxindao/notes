from flask import g
from functools import wraps

from rmon.common.rest import RestException


class ObjectMustBeExist:

    def __init__(self, object_class):
        """
        Args:
            object_class (class): 数据库对象
        """

        self.object_class = object_class

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            """
            Args:
                object_id (int): SQLAlchemy object id
            """

            object_id = kwargs.get('object_id')
            if object_id is None:
                raise RestException(404, 'object not exist')

            obj = self.object_class.query.get(object_id)
            if obj is None:
                raise RestException(404, 'object not exist')

            g.instance = obj
            return func(*args, **kwargs)

        return wrapper


class cached_property:
    pass
