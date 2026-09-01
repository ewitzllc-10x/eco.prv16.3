from flask import Flask, request, render_template_string, abort
import json, os
from pathlib import Path
from datetime import datetime
from functools import wraps
try:
 from dotenv import load_dotenv
 load_dotenv()
except: pass
ROOT = Path.home() / "eco.prv16.3"
ORDERS = ROOT / "adm_ewitz" / "orders.json"
SEAL_FILE = ROOT / "SOVEREIGNTY.txt"
SOVEREIGN_KEY = os.getenv("SOVEREIGN_KEY","UNSET")
if not SEAL_FILE.exists():
 SEAL_FILE.write_text(f"ECO.PRV16.3-{datetime.now().date()}-STALLION-10X-SOVEREIGN")
print(f"[SEAL] {SEAL_FILE.read_text().strip()[:60]}")
print(f"[KEY] {SOVEREIGN_KEY[:8]}...")
app = Flask(__name__)
def require_auth(f):
 @wraps(f)
 def d(*a, **k):
  prov = request.headers.get("X-SOVEREIGN-KEY") or request.args.get("key") or request.form.get("s_key")
  if prov != SOVEREIGN_KEY: abort(401, "KEY REQUIRED ?key=YOUR_KEY")
  return f(*a, **k)
 return d
HTML = """<!doctype html><html><head><meta name=viewport content="width=device-width,initial-scale=1"><title>Sovereign O.S - LOCKED</title><style>*{margin:0;padding:0;box-sizing:border-box}body{background:#0a0a0a;color:#00ff41;font-family:'Courier New',monospace;padding:20px;min-height:100vh}.os-title{color:#ff0040;text-shadow:0 0 15px #ff0040;font-size:28px;letter-spacing:3px;text-align:center;font-weight:bold}h1{color:#00ff41;text-shadow:0 0 10px #00ff41;margin:10px 0}input{background:#111;color:#00ff41;border:1px solid #00ff41;padding:15px;font-size:16px;flex:1}button{background:#00ff41;color:#0a0a0a;border:none;padding:15px 30px;font-weight:bold;cursor:pointer}.log{border:1px solid #00ff41;padding:15px;height:400px;overflow-y:auto;background:#050505}</style></head><body><div class=os-title>SOVEREIGN O.S - LOCKED</div><h1>ADM CONSOLE - {{seal}}</h1><form method=post><input type=hidden name=s_key value="{{sk}}"><input name=mission placeholder="mission..." autofocus autocomplete=off><button>DISPATCH [AUTHED]</button></form><div class=log><pre>{{log}}</pre></div></body></html>"""
@app.route('/', methods=['GET','POST'])
@require_auth
def index():
 log=""
 if request.method=='POST':
  m=request.form['mission'].strip()[:2000]
  if m:
   ORDERS.parent.mkdir(parents=True, exist_ok=True)
   d=json.loads(ORDERS.read_text()) if ORDERS.exists() else []
   if not isinstance(d, list): d=[]
   d.append(m)
   ORDERS.write_text(json.dumps(d, indent=2))
   log=f"DISPATCHED: {m}\n"
 if ORDERS.exists():
  try:
   q=json.loads(ORDERS.read_text())
   log+=f"\nQUEUE: {len(q)}\n"+"\n".join(q[-8:])
  except: pass
 return render_template_string(HTML, log=log, seal=SEAL_FILE.read_text().strip()[:80], sk=SOVEREIGN_KEY)
if __name__=='__main__':
 print(f"[SOVEREIGN O.S] LOCKED | BIND 127.0.0.1:5000 ONLY")
 print(f"[SOVEREIGN O.S] ACCESS: http://127.0.0.1:5000?key={SOVEREIGN_KEY}")
 app.run(host='127.0.0.1', port=5000, debug=False)
