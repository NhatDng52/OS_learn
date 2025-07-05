def lookup(name,lst,func):
        for x in lst:
            if name == func(x):
                return x
        return None