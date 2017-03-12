from django.test import TestCase

from apps.core.testing.mixins import (
    TestListViewMixin,
    TestModelAPIViewMixin,
    TestListAPIViewMixin
)

from .models import Catalog, Section, Subsection, QuestionEntity, Question


class QuestionsTestCase(TestCase):

    lang = 'en'

    fixtures = (
        'users.json',
        'groups.json',
        'accounts.json',
        'conditions.json',
        'domain.json',
        'options.json',
        'questions.json',
    )

    users = (
        ('editor', 'editor'),
        ('reviewer', 'reviewer'),
        ('user', 'user'),
        ('anonymous', None),
    )


class QuestionsTests(TestListViewMixin, QuestionsTestCase):

    url_names = {
        'list': 'catalogs'
    }
    status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 302}
    }


class CatalogTests(TestModelAPIViewMixin, QuestionsTestCase):

    instances = Catalog.objects.all()

    api_url_name = 'questions:catalog'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'retrieve': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'create': {'editor': 201, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'update': {'editor': 200, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'delete': {'editor': 204, 'reviewer': 403, 'user': 403, 'anonymous': 403}
    }

    def prepare_create_instance(self, instance):
        instance.key += '_new'
        return instance


class SectionTests(TestModelAPIViewMixin, QuestionsTestCase):

    instances = Section.objects.all()

    api_url_name = 'questions:section'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'retrieve': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'create': {'editor': 201, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'update': {'editor': 200, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'delete': {'editor': 204, 'reviewer': 403, 'user': 403, 'anonymous': 403}
    }

    def prepare_create_instance(self, instance):
        instance.key += '_new'
        return instance


class SubsectionTests(TestModelAPIViewMixin, QuestionsTestCase):

    instances = Subsection.objects.all()

    api_url_name = 'questions:subsection'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'retrieve': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'create': {'editor': 201, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'update': {'editor': 200, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'delete': {'editor': 204, 'reviewer': 403, 'user': 403, 'anonymous': 403}
    }

    def prepare_create_instance(self, instance):
        instance.key += '_new'
        return instance


class QuestionSetTests(TestModelAPIViewMixin, QuestionsTestCase):

    instances = QuestionEntity.objects.filter(question=None)

    api_url_name = 'questions:questionset'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'retrieve': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'create': {'editor': 201, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'update': {'editor': 200, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'delete': {'editor': 204, 'reviewer': 403, 'user': 403, 'anonymous': 403}
    }

    def prepare_create_instance(self, instance):
        instance.key += '_new'
        return instance


class QuestionTests(TestModelAPIViewMixin, QuestionsTestCase):

    instances = Question.objects.all()

    api_url_name = 'questions:question'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'retrieve': {'editor': 200, 'reviewer': 200, 'user': 403, 'anonymous': 403},
        'create': {'editor': 201, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'update': {'editor': 200, 'reviewer': 403, 'user': 403, 'anonymous': 403},
        'delete': {'editor': 204, 'reviewer': 403, 'user': 403, 'anonymous': 403}
    }

    def prepare_create_instance(self, instance):
        instance.key += '_new'
        return instance


class WidgetTypeTests(TestListAPIViewMixin, QuestionsTestCase):

    api_url_name = 'questions:widgettype'
    api_status_map = {
        'list': {'editor': 200, 'reviewer': 200, 'user': 200, 'anonymous': 200}
    }