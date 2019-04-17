"""Tests to verify that the template works as intended."""


def test_create_project(cookies):
    result = cookies.bake(extra_context={'app_name': 'a_new_function'})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == 'a_new_function'
    assert result.project.isdir()
