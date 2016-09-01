from _collections import OrderedDict
a = dict(a=10, b=20)
print(a['a'])
#print(a['c']) error
print(a.get('a'))
print(a.get('c')) #None
# No error

class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    


e=OrderedDict(a)
print(e)