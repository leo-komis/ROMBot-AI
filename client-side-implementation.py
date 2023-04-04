import openapi_client
from openapi_client.rest import ApiException

# Configure API client
api_client = openapi_client.ApiClient()
api_client.configuration.host = "https://api.openai.com/v1/completions"

# Instantiate API class
api_instance = openapi_client.CompletionsApi(api_client)

# Create completion request
completion_request = openapi_client.CompletionRequest(prompt="How may I be of assistance?", max_tokens=512)

# Call API
try:
    api_response = api_instance.create_completion(completion_request)
    print(api_response)
except ApiException as e:
    print("Exception when calling CompletionsApi->create_completion: %s\n" % e)

