class DbObject(object):
    def __init__(self, **args):
        for (column, value) in args.iteritems():
            setattr(self, column, value)
