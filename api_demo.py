import time
import graphsense
from pprint import pprint
from graphsense.api import addresses_api
from graphsense.model.address import Address
from graphsense.model.address_tags import AddressTags
from graphsense.model.address_txs import AddressTxs
from graphsense.model.entity import Entity
from graphsense.model.height import Height
from graphsense.model.links import Links
from graphsense.model.neighbor_addresses import NeighborAddresses
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
with graphsense.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    currency = "btc" # str | The cryptocurrency code (e.g., btc)
    address =  "211030fea2de89154373bebcae13751f8473ae423a966cbf0a9b69382138f215" # str | The cryptocurrency address

    try:
        # Get an address
        api_response = api_instance.get_address(currency, address)
        pprint(api_response)
    except graphsense.ApiException as e:
        print("Exception when calling AddressesApi->get_address: %s\n" % e)
