#!/usr/bin/env python3
import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcsms.v1.region.csms_region import CsmsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcsms.v1 import *


HW_ACCESS_KEY = os.getenv('HW_ACCESS_KEY')
HW_SECRET_KEY = os.environ.get('HW_SECRET_KEY')
HW_REGION_NAME = os.environ.get('HW_REGION_NAME')
HW_PROJECT_ID = os.environ.get('HW_PROJECT_ID')
HW_SECRET_NAME = os.environ.get('HW_SECRET_NAME')


if __name__ == "__main__":
    ak = HW_ACCESS_KEY
    sk = HW_SECRET_KEY
    region = HW_REGION_NAME
    projectId = HW_PROJECT_ID
    secretName = HW_SECRET_NAME

    credentials = BasicCredentials(ak, sk) \

    client = CsmsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(CsmsRegion.value_of(region)) \
        .build()

    try:
        request = ListSecretVersionsRequest()
        request.secret_name = secretName
        response = client.list_secret_versions(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)