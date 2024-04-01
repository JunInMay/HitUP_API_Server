from .common_constants import *

BASE_URI = BASE_LOCAL_URI

GOOGLE_CLIENT_ID = "구글 클라이언트 아이디"
GOOGLE_CLIENT_SECRET = "구글 시크릿 비밀번호"

GOOGLE_REDIRECT_URI = f"{BASE_URI}/accounts/google/login/callback/"

GOOGLE_LOGIN_REDIRECT_URI = (
        f"{BASE_GOOGLE_URL}"
        f"response_type={'code'}"
        f"&scope={GOOGLE_SCOPES}"
        f"&access_type={'online'}"
        f"&include_grant_scopes={'true'}"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
    )
