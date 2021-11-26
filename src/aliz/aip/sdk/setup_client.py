from aliz.aip.sdk.api_client import ApiClient
from aliz.aip.sdk.configuration import Configuration
from aliz.aip.sdk.environments import ENVIRONMENTS
from aliz.aip.token.token import TokenProvider


def setup_api_client(environment="prod"):
    """ Setup an API client object to interact with Aliz AIP SDK APIs

    :param environment: the name of the Aliz AIP environment to connect to
    :type environment: str, choice of ["prod", "dev", "local"]
    :return: an ApiClient object
    """
    environment = ENVIRONMENTS[environment]
    token_provider = TokenProvider.from_authentication_flow(environment.client_id, environment.client_secret)
    return setup_api_client_custom(environment.host, token_provider.get_token)


def setup_api_client_custom(host, token_provider):
    """ Setup an API client object to interact with Aliz AIP SDK APIs

    :param host: the URL to the Aliz AIP API server
    :type host: str
    :param token_provider: a callback function with no arguments that provides valid Google IAP tokens
    :type token_provider: function
    :return: an ApiClient object
    """
    def update_token(config):
        config.api_key = {"Authorization": token_provider()}

    configuration = Configuration()
    configuration.host = host
    configuration.api_key["Authorization"] = ""
    configuration.api_key_prefix["Authorization"] = "Bearer"
    configuration.refresh_api_key_hook = update_token
    return ApiClient(configuration)
