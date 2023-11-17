class InteractionDataStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InteractionDataStore, cls).__new__(cls)
            # Initialize your data store
            cls._instance.interactions = {}
        return cls._instance


# This function provides a global access point to the instance
def get_data_store():
    return InteractionDataStore()
