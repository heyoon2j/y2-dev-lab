import subprocess
import yaml

def execute_script(script):
    subprocess.run(script, shell=True, chekc=True)


def read_yaml(path, key):
    try:
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
        return config[key]
    except FileNotFoundError:
        print(f"[Error] {path} file not found")
    except Exception as e:
        print(f"[Error] {e}")

