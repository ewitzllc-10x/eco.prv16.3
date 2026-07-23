import subprocess
import tempfile
import os
from typing import Dict, Union

class CodeExecutor:
    def __init__(self, timeout: int = 5, max_output: int = 10000):
        self.timeout = timeout
        self.max_output = max_output
    
    def execute(self, code: str, language: str = "python") -> Dict[str, Union[str, int]]:
        """
        Execute code safely in a sandboxed subprocess.
        
        Args:
            code: The source code to execute
            language: Programming language (currently supports 'python')
        
        Returns:
            Dict with status, output, and error info
        """
        if not code or not isinstance(code, str):
            return {"status": "error", "output": "", "error": "Invalid code input"}
        
        # Write code to temp file
        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(code)
            temp_path = f.name
        
        try:
            # Run in restricted subprocess
            result = subprocess.run(
                ['python', temp_path],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            output = result.stdout[:self.max_output]
            error = result.stderr[:self.max_output] if result.stderr else None
            
            if result.returncode != 0:
                return {
                    "status": "error",
                    "output": output,
                    "error": error,
                    "returncode": result.returncode
                }
            
            return {
                "status": "success",
                "output": output,
                "error": None
            }
            
        except subprocess.TimeoutExpired:
            return {"status": "timeout", "output": "", "error": f"Execution exceeded {self.timeout}s"}
        except Exception as e:
            return {"status": "error", "output": "", "error": str(e)}
        finally:
            # Cleanup
            try:
                os.unlink(temp_path)
            except OSError:
                pass
