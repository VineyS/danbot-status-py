class APIError(Exception):
    """
    Raised when API returns an error
    """
    pass

class NodeError(Exception):
    """
    Raised when a node is not found.
    """
    pass

class NodeNegativeError(Exception):
    """
    Raised when a node number is negative.
    """
    pass

class LavaError(Exception):
    """
    Raised when a lava node is not found.
    """
    pass

class LavaNegativeError(Exception):
    """
    Raised when a lava node number is negative.
    """
    pass

