# My implementation of a HashMap.  Based off of the Java API for a HashMap.
# Includes get(), put(), keySet(), size(), containsKey(), and remove()

class hashmap:
    
    # Constructor
    def __init__(self, size):
        self.size = size
        self.table = self.makeTable()
    
    # Returns a list of lists, with nested lists representing the buckets
    def makeTable(self):
        return [[] for i in range(self.size)]
    
    # Store each key, value pair as a tuple in its corresponding bucket.
    def put(self, key, value):
        # some stuff
        return
    
    # Retrieve the value associated with key if it exists.  Otherwise, return None.
    def get(self, key):
        # some stuff
        return

    # Return the size of this HashMap
    def size(self):
        return self.size
    
    