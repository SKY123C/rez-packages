name = 'PythonFBX'

version = '0.1'

authors = ['chentao']

build_command = ""

def pre_build_commands():
    import os
    #print(env.PATH)
    env.FBXSDK_ROOT.append(os.path.join(build.build_path, "FBX/FBX SDK/2020.3.9"))
    env.FBXSDK_COMPILER.append("vs2022")
    import subprocess
    popen = subprocess.run(["python.exe", "-m", "pip", "install", "--force-reinstall", "-v", "sip==6.6.2"], check=True)
    subprocess.run(["python.exe", "-m", "pip", "install", "--target=C:/PythonFBX", os.path.join(build.build_path, "FBX/FBX Python Bindings/2020.3.9")], check=True)
