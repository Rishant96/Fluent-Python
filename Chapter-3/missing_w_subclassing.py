# Setup

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

# Test Case:

d = StrKeyDict0([('2', 'two'), ('4', 'four')])

# Item retrieval using the 'd[key]' notation:

print(d['2'])
print(d[4])
try:
    d[1]
except Exception as e:
    print(f'Error finding: {e}')

# Item retrieval using the 'd.get(key)' notation:

print(d.get('2'))
print(d.get(4))
print(d.get(1))
