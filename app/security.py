import hashlib


def get_client_id(site_id: str, user_agent: str, user_ip: str) -> str:
    """
    Generate a client ID for the given site ID, user agent, and IP address.

    :param site_id: The ID of the site being visited.
    :param user_agent: The user agent of the client.
    :param user_ip: The IP address of the client.
    :return: A client ID.
    """
    return hashlib.sha512((site_id + user_agent + user_ip).encode("utf-8")).hexdigest()
