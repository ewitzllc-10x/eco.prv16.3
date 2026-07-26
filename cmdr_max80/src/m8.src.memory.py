import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
STORE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memory_store.json")
mem = {}
if os.path.exists(STORE):
    try: mem = json.load(open(STORE))
    except: mem = {}

class H(BaseHTTPRequestHandler):
    def log_message(self, *a): return
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(mem).encode())
    def do_POST(self):
        global mem
        n = int(self.headers.get('Content-Length',0))
        body = self.rfile.read(n).decode() if n else ""
        try: j=json.loads(body) if body else {}
        except: j={}
        if "params" in j and isinstance(j["params"],dict):
            p=j["params"]
            j=p.get("arguments", p) if isinstance(p,dict) else p
        key=j.get("key"); val=j.get("value")
        res={}
        if key and val is not None:
            mem[key]=val
            res={"status":"remembered","key":key}
            try: open(STORE,"w").write(json.dumps(mem,indent=2))
            except: pass
        elif key:
            res=mem.get(key, {"status":"not_found","key":key})
        else:
            res=mem
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(res).encode())
        print(f"[MEM] {j} -> total={len(mem)}", flush=True)

print(f"[MEMORY] Booted 127.0.0.1:9749 -> {STORE}", flush=True)
HTTPServer(("127.0.0.1",9749), H).serve_forever()
