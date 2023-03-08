import pytest


@pytest.mark.valid
def test_login_valid1():
    print("Test case valid 1 Execute.")


@pytest.mark.valid
def test_login_valid2():
    print("Test case valid 2 Execute.")


@pytest.mark.invalid
def test_login_invalid1():
    print("Test invalid 1 Execute.")


@pytest.mark.invalid
def test_login_invalid2():
    print("Test invalid 2 Execute.")
