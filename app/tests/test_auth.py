


def test_signup(signup_user):
  assert signup_user.status_code == 200


def test_login_without_token(login_without_token):
  assert login_without_token.status_code == 422


def test_login_with_token(login_with_token):
  assert "Authorization" in login_with_token
  assert login_with_token["Authorization"].startswith("Bearer ")