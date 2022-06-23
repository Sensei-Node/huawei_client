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
HW_SECRET_VERSION = os.environ.get('HW_SECRET_VERSION')


if __name__ == "__main__":
    ak = HW_ACCESS_KEY
    sk = HW_SECRET_KEY
    region = HW_REGION_NAME
    projectId = HW_PROJECT_ID
    secretName = HW_SECRET_NAME
    secretVersion = HW_SECRET_VERSION

    credentials = BasicCredentials(ak, sk, projectId) \

    client = CsmsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(CsmsRegion.value_of(region)) \
        .build()

    try:
        request = ShowSecretVersionRequest()
        request.secret_name = secretName
        request.version_id = secretVersion
        response = client.show_secret_version(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)