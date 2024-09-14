import requests
from functions.othor import Othor as othor
import os

Othor = othor()

class Client:
    def __init__(self, url):
        self.url = url
        return

    def send_files(self, files: list):
        if len(files) == 0:
            Othor.error(text='Please input files.')
            return False
        else:
            files_obj = {}
            for file in files:
                if os.path.isfile(file):
                    # 送信
                    Othor.log(text='Analysis file >> {}'.format(file))
                    basename = os.path.basename(file)
                    files_obj[basename] = open(file, mode='rb')
                    pass
                else:
                    Othor.error(text='{} is not a file.'.format(file))
                    pass

                pass

            Othor.log('Send files...')
            response = None
            try:
                response = requests.post(self.url, files=files_obj)
            except Exception as e:
                Othor.error(text=str(e))
                return False

            if response.status_code == 200:
                if response.text == 'Failed': # 送信に失敗したとき
                    Othor.error('Failed to send files.')
                elif response.text == 'Done':
                    Othor.log('Done send files.')
                    return True

            return False