## Write API tests.

2 hours


### Resources

Django testing: https://docs.djangoproject.com/en/3.2/topics/testing/

unittest API: https://docs.python.org/3/library/unittest.html#unittest.TestCase

DRF testing tools: https://www.django-rest-framework.org/api-guide/testing/

Example of well-written Django/DRF test suite (Netbox): https://github.com/netbox-community/netbox/blob/develop/netbox/dcim/tests/test_api.py


## Basic model validation

Brainstorm:
- Haves, Passes, and Shows players and cards' Games must be consistent.
- Haves and Passes cannot contradict each other.
- Haves and Passes cannot be duplicate.  (How to handle duplicate creation
  attempt?)
- Shows cannot be for all-passed cards.
- Player Haves cannot exceed hand_size.
- Player Passes cannot exceed ncards - hand_size.
- Card passes cannot exceed nplayers.


## Firewall API views to enforce game-consistency

Require all Player, Card, Have, Pass, and Show list views to refer to a
specific game in order to retrieve data.

https://www.django-rest-framework.org/api-guide/filtering/#custom-generic-filtering


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

Here is how Netbox does choices: https://github.com/netbox-community/netbox/blob/27c0e6dd5e8732483533dbf3d4333a81fe9e7948/netbox/dcim/choices.py#L135


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
