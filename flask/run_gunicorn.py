import subprocess

command = ['python', '-m','gunicorn', '--config', 'gunicorn_config.py', 'server:application']
subprocess.run(command, shell=True)