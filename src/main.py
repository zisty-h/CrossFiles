from functions.client import *
from functions.server import *

def main():
    mode = input('Input Mode (Server or Client or Exit) >> ').lower()
    if mode == 'server':
        print('Please input port number to use server. Default port is 50')
        port = 50
        try:
            port: int = int(input('Input Port >> '))
        except Exception as e:
            print(e)
            print("Because server's port is 50")
            pass

        print("Please input True or False. If input word is True, Server's statue will public else, Server's statue will private.")
        isPublic = False
        try:
            isPublic: bool = bool(input('Input True or False >> '))
        except Exception as e:
            print(e)
            print("Because server's statue is False")
            pass

        app = Server(port=port, tunnel=isPublic)
        app.run()

        pass
    elif mode == 'client':
        url = input('Server URL >> ')

        if url[-1] == "/":
            url = url[:-1]

        try:
            res = requests.get(url + "/auth")
        except Exception as e:
            print(e)
            return

        if not res.text == 'Ok':
            return

        client = Client(url)
        files = []

        while True:
            file = input('File (path or exit) >> ')
            if file == 'exit':
                break

            if os.path.isfile(file):
                files.append(file)
            else:
                Othor.error('{} is not file'.format(file))

        client.send_files(files=files)
        pass
    elif mode == 'exit':
        exit()
    else:
        print('Please input server or client or exit.')
        pass

    return

if __name__ == '__main__':
    try:
        print(open('Promotion', 'r').read())
    except:
        print('Promotion file not found')
    while True:
        main()