from utilsMini import entity
import json
import datetime


class fff(entity.Entity):
    def __init__(self, **kwargs):
        super(fff, self).__init__(**kwargs)

    a = entity.IntgerType()
    e = entity.FloatType()
    f = entity.DateTimeType()
    g = entity.DictionaryType()


class aaa(entity.Entity):
    def __init__(self, **kwargs):
        super(aaa, self).__init__(**kwargs)

    a = entity.IntgerType()
    b = entity.ListType(fff)
    c = entity.ObjectType(fff)
    d = entity.StringType()
    e = entity.FloatType()
    f = entity.DateTimeType()
    g = entity.DictionaryType()
    z = entity.StringType("z")
    j = entity.ListType(entity.IntgerType)


dic = {
    "a":
    1,
    "b": [
        {
            "a": 1,
            "e": 1.2,
            "f": "2019-07-07 09:18:15",
            "g": {
                "ddd": 11
            },
        },
        {
            "a": 2,
            "e": 2.2,
            "f": "2019-07-08",
            "g": {
                "ddd": 22
            },
        },
    ],
    "c": {
        "a": 3,
        "e": 3.2,
        "f": "2019-07-09",
        "g": {
            "ddd": 33
        },
    },
    "d":
    "123",
    "e":
    1.6,
    "f":
    "2019-07-09",
    "g": {
        "ddd": 44
    },
    "j": [1]
}


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


er = aaa(**dic)
er2 = aaa()
er2.z = 'q'
print(er2.z)
print(json.dumps(er, cls=DateEncoder))
