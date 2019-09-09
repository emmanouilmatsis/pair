import rpyc

conn = rpyc.connect("localhost", 1337)
conn.root.print("OK")
