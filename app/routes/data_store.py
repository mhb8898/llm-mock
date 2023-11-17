"""
This module provides a singleton data store for managing chat interactions
in a FastAPI application.

The core component of this module is the `InteractionDataStore` class,
which implements the singleton design pattern. This ensures that there
is only one instance of the data store throughout the application lifecycle,
providing a centralized and consistent storage mechanism for interaction data.

The `get_data_store` function serves as a global accessor to the singleton
instance of the `InteractionDataStore`. This function simplifies the process
of obtaining the data store instance across the application.

The module plays a critical role in managing the state of chat interactions,
maintaining the integrity and consistency of the interaction data.

Classes:
- InteractionDataStore: A singleton class to manage the storage and
retrieval of interaction data.

Functions:
- get_data_store: Returns the singleton instance of the InteractionDataStore.
"""


# pylint: disable=R0903
class InteractionDataStore:
    """
    A singleton class that serves as a central data store for all
    interactions in the application.

    This class uses the singleton design pattern to ensure that there's only
    one instance of the data store
    throughout the application. This instance is used to store and manage interactions.

    Attributes:
        interactions (dict): A dictionary that stores interaction objects,
        typically keyed by interaction IDs.

    The singleton instance is created upon the first instantiation and reused thereafter.
    """

    _instance = None
    interactions = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InteractionDataStore, cls).__new__(cls)
            # Initialize your data store
            cls._instance.interactions = {}
        return cls._instance


# This function provides a global access point to the instance
def get_data_store():
    """
    Provides global access to the singleton instance of InteractionDataStore.

    This function is used throughout the application to access the single, shared instance of the
    InteractionDataStore class, ensuring that interaction data is centrally managed and consistent.

    Returns:
        InteractionDataStore: The singleton instance of the InteractionDataStore.
    """
    return InteractionDataStore()
