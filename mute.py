from samsungtvws import SamsungTVWS
import os

TV_IP = '192.168.1.105'

token_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'tv_token.txt'
)

print("Token path:", token_path)

try:
    print(f"Connecting to Samsung TV at {TV_IP}...")

    tv = SamsungTVWS(
        host=TV_IP,
        port=8002,
        token_file=token_path,
        timeout=10,
        name='RonRemote'
    )

    print("Sending Mute up command...")
    tv.send_key('KEY_MUTE')
    print("Volume Mute command sent.")

except Exception as e:
    print("ERROR:", repr(e))



