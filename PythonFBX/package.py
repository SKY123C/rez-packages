name = 'PythonFBX'

version = '0.1'

authors = ['chentao']

build_command = ""

def pre_build_commands():
    import os
    import subprocess
    copy_env = os.environ.copy()
    copy_env["FBXSDK_ROOT"] = os.path.join(build.build_path, "FBX/FBX SDK/2020.3.9")
    copy_env["FBXSDK_COMPILER"] = "vs2022"
    fbx_bindings_path = os.path.join(build.build_path, "FBX/FBX Python Bindings/2020.3.9")
    popen = subprocess.run(["python.exe", "-m", "pip", "install", "--force-reinstall", "-v", "sip==6.6.2"], check=True)
    subprocess.run(["python.exe", "-m", "pip", "install", "--target=C:/PythonFBX", fbx_bindings_path], env=copy_env, check=True)

