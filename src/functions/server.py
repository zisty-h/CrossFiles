import sys
from flask import *
from functions.othor import Othor as othor
from pyngrok import ngrok

Othor = othor()

class Server:
    def __init__(self, port: int, tunnel: bool = False):
        self.port = port
        self.tunnel = tunnel

    app = Flask(__name__)

    def run(self):
        print('Close >> Ctrl+C')
        @self.app.route('/', methods=['POST'])
        def index():
            if len(request.files) == 0:
                Othor.error(text="This request don't have any files")
                return 'Failed'
            else:
                files = request.files
                for file in files:
                    Othor.log(text='Analysis file >> {}'.format(file))
                    try:
                        with open('./' + file, 'wb') as f:
                            Othor.log(text='Downloading file...')
                            f.write(files[file].read())
                    except Exception as e:
                        Othor.error(text='Error: {}'.format(e))
                        continue

                    Othor.log(text='Done Downloading file.')

                print('End All Download.')

                return 'Done'

        @self.app.route('/auth', methods=['GET'])
        def auth():
            return 'Ok'

        if self.tunnel:
            client = ngrok.connect(str(self.port))
            print('Public url is {}'.format(client.public_url))
        self.app.run(port=self.port)


