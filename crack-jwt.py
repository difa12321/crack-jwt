import jwt
import termcolor
jwt_str = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmFuYSIsImFjdGlvbiI6InVwbG9hZCJ9.56wwCrB9tIgmUnYpLPxkO8GYj1soCjuu_skTlbH_Gg8'
with open('/tmp/chinese_topl0000.txt') as f:
    for line in f:
        key_ = line.strip()
        try:
            jwt.decode(jwt_str, verify=True, key=key_)
            print('found key ---> ', termcolor.colored(key_, 'red'), '<---')
            break
        except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
            print('bingo! key --------> ', termcolor.colored(key_, 'green'), '<--------')
            break
        except jwt.exceptions.InvalidSignatureError:
            # print(' ' * 64, 'try', key_, end='', flush=True)
            continue
    else:
        print('sorry! no key be found.')
