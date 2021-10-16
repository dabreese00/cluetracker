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
