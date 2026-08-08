import pytest

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("admin","123456",True),
        ("admin","wrong",False),
        ("","",False)
    ]
)
def test_login(username,password,expected):

    print(
        f"账号:{username},密码:{password}"
    )

    if username == "admin" and password == "123456":
        result = True
    else:
        result = False

    assert result == expected