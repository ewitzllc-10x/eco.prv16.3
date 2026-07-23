import json, http.client, socket
class MCPMemory:
    def __init__(self, host="127.0.0.1", port=9749):
        self.host = host; self.port = port
    def _send(self, payload):
        try:
            conn = http.client.HTTPConnection(self.host, self.port, timeout=1)
            conn.request("POST","/",body=json.dumps(payload),headers={"Content-Type":"application/json"})
            data = conn.getresponse().read().decode()
            conn.close()
            return json.loads(data) if data else {}
        except:
            try:
                with socket.create_connection((self.host,self.port),timeout=1) as s:
                    s.sendall((json.dumps(payload)+"\n").encode())
                    return json.loads(s.recv(4096).decode())
            except:
                return None
    def remember(self, key, value):
        self._send({"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"remember","arguments":{"key":key,"value":str(value)}}})
        return True
    def recall(self, key):
        r = self._send({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"recall","arguments":{"key":key}}})
        return r
