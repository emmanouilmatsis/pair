import rpyc

class MyService(rpyc.Service):
    def on_connect(self, conn):
        print("on_connect")

    def on_disconnect(self, conn):
        print("on_disconnect")

    def exposed_print(self, text):
        print(text)

if __name__ == "__main__":
    rpyc.utils.server.ThreadedServer(MyService, port=1337).start()
