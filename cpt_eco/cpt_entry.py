from importlib.util import spec_from_file_location, module_from_spec

def load(path, name):
    spec = spec_from_file_location(name, path)
    mod = module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

cpt = load('cpt_eco/cpt_workflows/cpt_workflow.main.py', 'cpt')
lt1 = load('cpt_eco/1lt_action/1lt_workflows/1lt_workflow.main.py', 'lt1')
lt2 = load('cpt_eco/2lt_devil_dog/2lt_workflows/2lt_workflow.main.py', 'lt2')

print("=== ECO PRV16.3 FULL CHAIN EXECUTION ===")
cmd = "MISSION: SECURE BLUE STATUS"
print(cpt.CptWorkflow().execute(cmd))
print(lt1.Lt1Workflow().execute(cmd))
print(lt2.Lt2Workflow().execute(cmd))
print("=== ALL UNITS BLUE ===")
