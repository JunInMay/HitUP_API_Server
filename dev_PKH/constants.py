GOOGLE_CLIENT_ID = "" # 구글 클라이언트 아이디
GOOGLE_CLIENT_SECRET = "" # 구글 클라이언트 비밀번호

BASE_URI = 'http://hitup.shop:8000'
#BASE_URI = 'http://54.180.88.188:8000'
#BASE_URI = 'http://127.0.0.1:8000'
BASE_GOOGLE_URL = "https://accounts.google.com/o/oauth2/v2/auth?"

GOOGLE_REDIRECT_URI = f"{BASE_URI}/accounts/google/login/callback/"

GOOGLE_SCOPES = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"

GOOGLE_LOGIN_REDIRECT_URI = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"response_type={'code'}"
        f"&scope={GOOGLE_SCOPES}"
        f"&access_type={'online'}"
        f"&include_grant_scopes={'true'}"
        f"&client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={GOOGLE_REDIRECT_URI}"
    )
