import os, pathlib
ROOT = pathlib.Path("~/eco.prv16.3").expanduser()
BRANCH = "pro16v3erbs"
CPT_ROOT = ROOT / "cpt_eco"
def status():
    return f"cpt_eco at {CPT_ROOT} on branch {BRANCH} - peers cmdr_max80 + adm_ewitz"
