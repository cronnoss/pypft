import pytest

from model.group import Group
from fixtura.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.session.create_group(Group(name="pytest1", header="pytest2", footer="pytest3"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.session.create_group(Group(name="", header="", footer=""))
    app.session.logout()