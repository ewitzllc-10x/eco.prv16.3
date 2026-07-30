import subprocess, time, psutil
RANKS = {
    "CPT": "cpt_eco/cpt_src/cpt_src.cmdr_link.py",
    "LT2": "cpt_eco/lt2_eco/lt2_eco.py", 
    "DD": "cpt_eco/devil_dogs/devil_dogs.py"
}
while True:
    for name, path in RANKS.items():
        if not any(path in " ".join(p.cmdline()) for p in psutil.process_iter()):
            print(f"[WATCHDOG] {name} DOWN - RESTARTING")
            subprocess.Popen(["python3", "-u", path], 
                           stdout=open(f"logs/{name.lower()}.out","a"))
    time.sleep(30)
