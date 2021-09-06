## Write API tests.

2 hours


### Resources

Django testing: https://docs.djangoproject.com/en/3.2/topics/testing/

unittest API: https://docs.python.org/3/library/unittest.html#unittest.TestCase

DRF testing tools: https://www.django-rest-framework.org/api-guide/testing/

Example of well-written Django/DRF test suite (Netbox): https://github.com/netbox-community/netbox/blob/develop/netbox/dcim/tests/test_api.py


## Write better model tests

2 hours

Observe how Netbox tests their models: https://github.com/netbox-community/netbox/blob/develop/netbox/dcim/tests/test_models.py

They are testing interactions.


## Look into why API doesn't seem to be requiring authentication


## Order querysets for serializers to make pagination consistent

1 hour

See warning message:

```
web_1  | /usr/local/lib/python3.9/site-packages/rest_framework/pagination.py:200: UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'games.models.Show'> QuerySet.
web_1  |   paginator = self.django_paginator_class(queryset, page_size)
```


## Add a "card type" field to Card model/serializer/viewset

1 hour

Otherwise, may run into the issue of seeing a Card but not knowing whether it's
a Person, Weapon, or Room.

Can possibly just add a property to the Card model whose value is `type(self)`?

Or, add a `card_type` to the base model, default to Null, and then have it
auto-initialized to hard-coded values for the subclasses?  Is that any better
than just reverting to having a card_type field as a Django TextChoice nested
class?


## Override the Game create view/serializer to improve workflow

Exploratory, more than 2 hours

Creating a game should ideally involve creating Players and Cards, without
breaking flow to do that separately.

Possible ways to handle:
- Have the create view pull pre-entered card set options from a source (a separate app or service?)
- Use Writable Nested Serialization for Players (and possibly Cards)

### Resources

https://www.django-rest-framework.org/api-guide/serializers/#writable-nested-representations
https://www.django-rest-framework.org/api-guide/serializers/#specifying-nested-serialization
https://github.com/beda-software/drf-writable-nested
