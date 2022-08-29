from imagekitio.models.results.ResponseMetadata import ResponseMetadata


class NotFoundException(Exception):

    def __init__(self, message, response_help, response_metadata: ResponseMetadata):
        self.message = message
        self.response_help = response_help
        print("here:-->", response_metadata.__dict__)
        self.response_metadata = response_metadata

    def __str__(self):
        return str(self.message)
