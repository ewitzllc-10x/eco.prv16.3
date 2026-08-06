from flask import Flask, request, render_template_string
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
ROOT = Path.home() / "eco.prv16.3"
ORDERS = ROOT / "adm_ewitz" / "orders.json"

HTML = """
<!doctype html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sovereign O.S | ADM CONSOLE</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0a0a;color:#00ff41;font-family:'Courier New',monospace;padding:20px;min-height:100vh}
.os-title{color:#ff0040;text-shadow:0 0 15px #ff0040;font-size:32px;letter-spacing:4px;margin-bottom:5px;text-align:center;font-weight:bold}
h1{color:#00ff41;text-shadow:0 0 10px #00ff41;margin-bottom:10px;font-size:24px}
.subtitle{color:#0080ff;margin-bottom:20px;font-size:14px}
.header{border:1px solid #ff0040;padding:15px;margin-bottom:20px;box-shadow:0 0 20px rgba(255,0,64,0.3)}
.status{display:inline-block;margin-right:20px}
form{display:flex;gap:10px;margin-bottom:20px}
input{background:#111;color:#00ff41;border:1px solid #00ff41;padding:15px;font-size:16px;font-family:monospace;flex:1}
input:focus{outline:none;box-shadow:0 0 10px #00ff41}
button{background:#00ff41;color:#0a0a0a;border:none;padding:15px 30px;font-size:16px;font-family:monospace;font-weight:bold;cursor:pointer}
button:hover{box-shadow:0 0 15px #00ff41}
.log{border:1px solid #00ff41;padding:15px;height:400px;overflow-y:auto;background:#050505}
.log pre{margin:0;line-height:1.6;white-space:pre-wrap}
.queue{color:#ffff00}
.success{color:#00ff41}
.error{color:#ff0040}
.timestamp{color:#0080ff}
.cmdr{color:#ff8000;font-weight:bold}
</style></head>
<body>
<div class="os-title">SOVEREIGN O.S</div>
<div class="header">
<h1>[ADM CONSOLE] ECO.PRV16.3</h1>
<div class="subtitle">DIRECT LINK TO <span class="cmdr">CMDR_MAX80</span> — SINGLE POINT OF CONTACT</div>
<span class="status">CHAIN: <span class="success">ONLINE</span></span>
<span class="status">DELEGATION: CMDR_MAX80→CPT_ECO→1LT_ACTION/2LT_DEVIL_DOG→DEVIL_DOGS</span>
</div>
<form method=post>
<input name=mission placeholder="build stallion_website, urgent: deploy services.html, status report, etc..." autofocus autocomplete=off>
<button type=submit>DISPATCH TO CMDR</button>
</form>
<div class=log><pre>{{log}}</pre></div>
<script>
// setTimeout(()=>location.reload(),3000);
document.querySelector('input').focus();
</script>
</body></html>
"""

@app.route('/', methods=['GET','POST'])
def index():
    log = ""
    if request.method == 'POST':
        mission = request.form['mission'].strip()
        if mission:
            ORDERS.parent.mkdir(parents=True, exist_ok=True)
            try:
                data = json.loads(ORDERS.read_text()) if ORDERS.exists() else []
            except: data = []
            data.append(mission)
            ORDERS.write_text(json.dumps(data, indent=2))
            ts = datetime.now().strftime('%H:%M:%S')
            log = f'<span class="timestamp">[{ts}]</span> <span class="success">DISPATCHED TO CMDR_MAX80:</span> {mission}\n'
    
    if ORDERS.exists():
        try:
            queue = json.loads(ORDERS.read_text())
            log += f'\n<span class="queue">CMDR QUEUE: {len(queue)} orders</span>\n'
            log += "\n".join([f"  > {q}" for q in queue[-8:]])
        except: pass
    
    cmdr_log = ROOT / "logs" / "cmdr.out"
    if cmdr_log.exists():
        lines = cmdr_log.read_text().split('\n')[-10:]
        log += f'\n\n<span class="timestamp">[CMDR_MAX80 LOG]</span>\n' + "\n".join(lines)
    
    return render_template_string(HTML, log=log)

if __name__ == '__main__':
    print("[SOVEREIGN O.S] ADM CONSOLE | CMDR_MAX80 LINK ACTIVE on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)
