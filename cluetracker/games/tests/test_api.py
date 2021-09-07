from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from django.forms.models import model_to_dict
from django.core.exceptions import FieldDoesNotExist
from django.db.models import ManyToManyField, ForeignKey
from rest_framework import status
from games.models import Game, Player, Card, Have, Pass, Show


class APITestCase(TestCase):
    """
    Base test class for API tests.

    Provides common methods useful for API tests.

    Heavily inspired by the Netbox community/Netbox project's ModelTestCase and
    APITestCase.
    """

    model = None
    view_namespace = None

    def setUp(self):
        self.user = User.objects.create_user(username='testuser')
        self.client = APIClient()

    def _get_queryset(self):
        """
        Return a base queryset suitable for use in test methods.
        """
        return self.model.objects.all()

    def _get_detail_url(self, instance):
        viewname = f'{instance._meta.model_name}-detail'
        return reverse(viewname, kwargs={'pk': instance.pk})

    def _get_list_url(self):
        viewname = f'{self.model._meta.model_name}-list'
        return reverse(viewname)

    def assertHttpStatus(self, response, expected_status):
        """
        Provide more detail in the event of an unexpected HTTP response.
        """
        err_message = None

        # Construct an error message only if we expect the test to fail
        if response.status_code != expected_status:
            if hasattr(response, 'data'):
                err = response.data
            else:
                err = 'No data'

            err_message = f"Expected status {expected_status}; received {response.status_code}: {err}"  # noqa: 501

        self.assertEqual(response.status_code, expected_status, err_message)

    def model_to_dict(self, instance, fields):
        """
        Return a dictionary representation of an instance.
        """
        # Call Django's model_to_dict() to extract all fields
        model_dict = model_to_dict(instance, fields=fields)

        # Map any additional (non-field) instance attributes that were
        # specified
        for attr in fields:
            if hasattr(instance, attr) and attr not in model_dict:
                model_dict[attr] = getattr(instance, attr)

        for key, value in list(model_dict.items()):
            try:
                field = instance._meta.get_field(key)
            except FieldDoesNotExist:
                # Attribute is not a model field
                continue

            # Convert ForeignKeys to hyperlinks
            if value and type(field) == ForeignKey:
                model_dict[key] = self._get_detail_url(getattr(instance, key))

            # Handle ManyToManyFields
            if value and type(field) == ManyToManyField:
                model_dict[key] = sorted([self._get_detail_url(obj) for obj in getattr(instance, key)])  # noqa: 501

        return model_dict

    def assertInstanceEqual(self, instance, data, exclude=None):
        """
        Compare a model instance to a dictionary, checking that its attribute
        values match those specified in the dictionary.

        :param instance: Python object instance
        :param data: Dictionary of test data used to define the instance
        :param exclude: List of fields to exclude from comparison
        """
        if exclude is None:
            exclude = []

        fields = [k for k in data.keys() if k not in exclude]
        model_dict = self.model_to_dict(instance, fields=fields)

        relevant_data = {
            k: v for k, v in data.items() if hasattr(instance, k) and k not in exclude  # noqa: 501
        }

        self.assertDictEqual(model_dict, relevant_data)


class APIViewTestCases():
    """Classes for testing Django Rest Framework API ViewSets.

    Heavily inspired by the Netbox project's API view tests.
    """

    class GetObjectViewTestCase(APITestCase):

        def test_get_object_anonymous(self):
            """
            GET a single object as an unauthenticated user.
            """
            url = self._get_detail_url(self._get_queryset().first())

            self.assertHttpStatus(
                self.client.get(url),
                status.HTTP_403_FORBIDDEN
            )

        def test_get_object(self):
            """
            GET a single object as an authenticated user.
            """
            url = self._get_detail_url(self._get_queryset().first())

            self.client.force_login(self.user)

            self.assertHttpStatus(
                self.client.get(url),
                status.HTTP_200_OK
            )

    class ListObjectsViewTestCase(APITestCase):

        def test_list_objects_anonymous(self):
            """
            GET a list of objects as an unauthenticated user.
            """
            response = self.client.get(self._get_list_url())
            self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

        def test_list_objects(self):
            """
            GET a list of objects as an authenticated user.
            """
            self.client.force_login(self.user)

            response = self.client.get(self._get_list_url())
            self.assertHttpStatus(response, status.HTTP_200_OK)

            self.assertEqual(
                len(response.data['results']),
                self._get_queryset().count()
            )

    class CreateObjectViewTestCase(APITestCase):
        create_data = []

        def test_create_object_anonymous(self):
            """
            POST a single object as an unauthenticated user.
            """
            response = self.client.post(
                self._get_list_url(),
                self.create_data[0],
                format='json'
            )
            self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

        def test_create_object(self):
            """
            POST a single object as an authenticated user.
            """
            self.client.force_login(self.user)

            initial_count = self._get_queryset().count()
            response = self.client.post(
                self._get_list_url(),
                self.create_data[0],
                format='json'
            )
            self.assertHttpStatus(response, status.HTTP_201_CREATED)
            self.assertEqual(self._get_queryset().count(), initial_count + 1)

            instance = self._get_queryset().get(pk=response.data['id'])
            self.assertInstanceEqual(
                instance,
                self.create_data[0]
            )

    class UpdateObjectViewTestCase(APITestCase):
        update_data = {}

        def test_update_object_anonymous(self):
            """
            PATCH a single object as an unauthenticated user.
            """
            url = self._get_detail_url(self._get_queryset().first())
            update_data = self.update_data or getattr(self, 'create_data')[0]

            response = self.client.patch(url, update_data, format='json')
            self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

        def test_update_object(self):
            """
            PATCH a single object as an authenticated user.
            """
            self.client.force_login(self.user)

            instance = self._get_queryset().first()
            url = self._get_detail_url(instance)
            update_data = self.update_data or getattr(self, 'create_data')[0]

            response = self.client.patch(url, update_data, format='json')
            self.assertHttpStatus(response, status.HTTP_200_OK)
            instance.refresh_from_db()
            self.assertInstanceEqual(
                instance,
                update_data
            )

    class DeleteObjectViewTestCase(APITestCase):

        def test_delete_object_anonymous(self):
            """
            DELETE a single object as an unauthenticated user.
            """
            url = self._get_detail_url(self._get_queryset().first())
            response = self.client.delete(url)
            self.assertHttpStatus(response, status.HTTP_403_FORBIDDEN)

        def test_delete_object(self):
            """
            DELETE a single object as an authenticated user.
            """
            self.client.force_login(self.user)

            instance = self._get_queryset().first()
            url = self._get_detail_url(instance)
            response = self.client.delete(url)
            self.assertHttpStatus(response, status.HTTP_204_NO_CONTENT)
            self.assertFalse(self._get_queryset().filter(pk=instance.pk).exists())  # noqa: 501

    class APIViewTestCase(
        GetObjectViewTestCase,
        ListObjectsViewTestCase,
        CreateObjectViewTestCase,
        UpdateObjectViewTestCase,
        DeleteObjectViewTestCase
    ):
        pass


class GameViewTestCase(APIViewTestCases.APIViewTestCase):
    model = Game
    create_data = [
        {}
    ]

    @classmethod
    def setUpTestData(cls):

        Game.objects.create()


class PlayerViewTestCase(APIViewTestCases.APIViewTestCase):
    model = Player

    def setUp(self):
        super().setUp()

        game = Game.objects.create()
        Player.objects.create(name='Bob', hand_size=3, game=game)
        self.create_data = [
            {
                'name': 'Alice',
                'hand_size': 4,
                'game': self._get_detail_url(game)
            }
        ]


class CardViewTestCase(APIViewTestCases.APIViewTestCase):
    model = Card

    def setUp(self):
        super().setUp()

        game = Game.objects.create()
        Card.objects.create(
            name='Colonel Mustard',
            kind=Card.PERSON,
            game=game
        )
        self.create_data = [
            {
                'name': 'Ballroom',
                'kind': Card.ROOM,
                'game': self._get_detail_url(game)
            }
        ]


class ClueRelationViewTestCase(APITestCase):
    """Class that adds base data setup for testing ClueRelations"""

    def setUp(self):
        super().setUp()

        self.game = Game.objects.create()
        self.player1 = Player.objects.create(
            name='Bob',
            hand_size=3,
            game=self.game
        )
        self.player2 = Player.objects.create(
            name='Alice',
            hand_size=4,
            game=self.game
        )
        self.card1 = Card.objects.create(
            name='Colonel Mustard',
            kind=Card.PERSON,
            game=self.game
        )
        self.card2 = Card.objects.create(
            name='Rope',
            kind=Card.WEAPON,
            game=self.game
        )
        self.card3 = Card.objects.create(
            name='Ballroom',
            kind=Card.ROOM,
            game=self.game
        )


class HaveViewTestCase(APIViewTestCases.APIViewTestCase,
                       ClueRelationViewTestCase):
    model = Have

    def setUp(self):
        super().setUp()

        Have.objects.create(
            player=self.player1,
            card=self.card1,
            game=self.game
        )

        self.create_data = [
            {
                'player': self._get_detail_url(self.player2),
                'card': self._get_detail_url(self.card2),
                'game': self._get_detail_url(self.game)
            }
        ]


class PassViewTestCase(APIViewTestCases.APIViewTestCase,
                       ClueRelationViewTestCase):
    model = Pass

    def setUp(self):
        super().setUp()

        Pass.objects.create(
            player=self.player1,
            card=self.card1,
            game=self.game
        )

        self.create_data = [
            {
                'player': self._get_detail_url(self.player2),
                'card': self._get_detail_url(self.card2),
                'game': self._get_detail_url(self.game)
            }
        ]


class ShowViewTestCase(APIViewTestCases.APIViewTestCase,
                       ClueRelationViewTestCase):
    model = Show

    def setUp(self):
        super().setUp()

        Show.objects.create(
            player=self.player1,
            person=self.card1,
            weapon=self.card2,
            room=self.card3,
            game=self.game
        )

        self.create_data = [
            {
                'player': self._get_detail_url(self.player2),
                'person': self._get_detail_url(self.card1),
                'weapon': self._get_detail_url(self.card2),
                'room': self._get_detail_url(self.card3),
                'game': self._get_detail_url(self.game)
            }
        ]
