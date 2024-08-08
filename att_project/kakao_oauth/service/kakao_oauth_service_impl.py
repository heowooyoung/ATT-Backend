from att_project import settings
from kakao_oauth.service.kakao_oauth_service import KakaoOauthService

import requests


class KakaoOauthServiceImpl(KakaoOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.clientSecret = settings.KAKAO['CLIENT_SECRET']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def kakaoLoginAddress(self):
        print('kakaoLoginAddress()')
        return (f"{self.loginUrl}/oauth/authorize?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")

    def requestAccessToken(self, kakaoAuthCode):
        print("requestAccessToken()")
        accessTokenRequestForm = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': kakaoAuthCode,
            'client_secret': self.clientSecret
        }

        response = requests.post(self.tokenRequestUri, data=accessTokenRequestForm)
        return response.json()