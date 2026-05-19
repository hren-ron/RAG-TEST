

import os
import config_data as config

def check_md5(md5_str: str):

    if not os.path.exists(config.md5_path):
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False

    else:
        with open(config.md5_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() == md5_str:
                    return True
        return False

def save_md5(md5_str: str):

    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')

def get_str_md5(str_: str, encoding='utf-8'):

    import hashlib
    return hashlib.md5(str_.encode(encoding)).hexdigest()



class Kne   ologyBase:




if __name__ == '__main__':
    print(get_str_md5('123456'))
    print(check_md5(get_str_md5('123456')))