def login(username,password):
    if username == "admin" and password == "123456":
        return "登录成功"
    else:
        return "账号或密码错误"

def test_login_success():
    result = login("admin","123456")

    assert result == "登录成功"

def test_login_fail():
    result = login("admin","wrong")

    assert result == "账号或密码错误"