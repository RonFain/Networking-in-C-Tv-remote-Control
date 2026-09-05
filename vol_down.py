from samsungtvws import SamsungTVWS
import os
import time
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

    print("Sending Down up command...")
    tv.send_key('KEY_VOLDOWN', cmd='Press')
    time.sleep(0.5)
    tv.send_key('KEY_VOLDOWN', cmd='Release')

except Exception as e:
    print("ERROR:", repr(e))


