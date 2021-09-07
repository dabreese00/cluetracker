# Helpful resources

## Writing tests

### Models tests

Observe how Netbox tests their models: https://github.com/netbox-community/netbox/blob/develop/netbox/dcim/tests/test_models.py

### API tests

Django testing: https://docs.djangoproject.com/en/3.2/topics/testing/

unittest API: https://docs.python.org/3/library/unittest.html#unittest.TestCase

DRF testing tools: https://www.django-rest-framework.org/api-guide/testing/

Example of well-written Django/DRF test suite (Netbox): https://github.com/netbox-community/netbox/blob/develop/netbox/dcim/tests/test_api.py

## Designing Models

Here is how Netbox does choices: https://github.com/netbox-community/netbox/blob/27c0e6dd5e8732483533dbf3d4333a81fe9e7948/netbox/dcim/choices.py#L135
