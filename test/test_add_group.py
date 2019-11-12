from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="pytest1", header="pytest2", footer="pytest3"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


#   for testing ensure_login
#   app.session.logout()


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
