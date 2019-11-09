from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="pytest1", header="pytest2", footer="pytest3"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
