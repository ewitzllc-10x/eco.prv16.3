import ast, re
class CodeAnalyzer:
    def analyze(self, code: str):
        if not code or not code.strip():
            return {"status":"error","details":"empty","lines":0}
        lines = code.splitlines()
        info = {"status":"ok","lines":len(lines),"chars":len(code),"details":f"{len(lines)} lines"}
        try:
            tree = ast.parse(code)
            info["funcs"] = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
            info["imports"] = len([n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))])
            info["classes"] = len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
        except:
            info["funcs"]=len(re.findall(r'def\s+\w+',code))
            info["imports"]=len(re.findall(r'^\s*(import|from)\s+',code, re.M))
            info["classes"]=len(re.findall(r'class\s+\w+',code))
        return info
