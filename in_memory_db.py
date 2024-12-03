class InMemoryDB:
    def __init__(self) -> None:
        self.in_progress = False
        self.db = {} # <string: integer>
        self.uncommitted_changes = []

    def get(self, key):
        '''
        return the value associated with the key or null if the key
        doesn’t exist.
        can be called at any time, independent of if a transaction 
        is in progress.
        '''
        return self.db.get(key)
    
    def put(self, key, val):
        # throw exception if transaction not in progress
        if not self.in_progress:
            raise Exception('put error: transaction not in progress. To start a transaction call begin_transaction()')

        # Check if key is a string
        if not isinstance(key, str):
            raise TypeError("Key must be a string.")

        # Check if val is an integer
        if not isinstance(val, int):
            raise TypeError("Value must be an integer.")


        # add pair to uncommitted changes
        self.uncommitted_changes.append((key, val))

    def begin_transaction(self):
        # throw exception if transaction is already in progress
        if self.in_progress:
            raise Exception('begin_transaction error: At a time only a single transaction may exist.')
        
        self.in_progress = True
        

    def commit(self):
        if not self.in_progress:
            raise Exception("commit error: there is no ongoing transaction.")

        # end transaction
        self.in_progress = False
        
        # commit uncommitted changes
        for key, val in self.uncommitted_changes:
            self.db[key] = val

        # clear uncommitted changes
        self.uncommitted_changes = []

    def rollback(self):
        if not self.in_progress:
            raise Exception("rollback error: there is no ongoing transaction.")
        # end transaction
        self.in_progress = False

        # clear uncommitted changes
        self.uncommitted_changes = []