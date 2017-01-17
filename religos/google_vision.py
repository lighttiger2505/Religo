# [START import_libraries]
import base64

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
# [END import_libraries]


def do_ocr(photo_file):
    """Run a label request on a single image"""

    # [START authenticate]
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials)
    # [END authenticate]

    # [START construct_request]
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        # [END construct_request]
        # [START parse_response]
        response = service_request.execute()
        text = response['responses'][0]['textAnnotations'][0]['description']
        # print('Found text: %s for %s' % (text, photo_file))
        return text
        # [END parse_response]
