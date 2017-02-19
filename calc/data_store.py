class DataStore(object):
    store = dict()

    def __init__(self, store):
        DataStore.store = store

    @staticmethod
    def get_argument_value(token):
        if token.val in DataStore.store:
            return DataStore.store[token.val]
        else:
            raise NameError('Parameter ' + token.val + " doesn't exist")
