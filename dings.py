import time
import graphsense
from graphsense.api import entities_api
from graphsense.api import tags_api
from graphsense.model.height import Height
from graphsense.model.address_txs import AddressTxs
from pprint import pprint
# Defining the host is optional and defaults to https://api.ikna.io
# See configuration.py for a list of all supported configuration parameters.
configuration = graphsense.Configuration(
    host = "https://api.ikna.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'XvG+5WnFM50e7vlDlJX5rubGTZYRCIIh'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
# Enter a context with an instance of the API client
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tags_api.TagsApi(api_client)
    actor = "binance" # str | actor id

    # example passing only required values which don't have defaults set
    try:
        # Returns an actor given its unique id or (unique) label
        api_response = api_instance.get_actor(actor)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling TagsApi->get_actor: %s\n" % e)
