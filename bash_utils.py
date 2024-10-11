import subprocess

# Function to execute a bash command and get its output
def execute_command(command):
    """
    Executes a bash command and returns its output as a string.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

# Function to execute a bash command and get both stdout and stderr
def execute_command_full(command):
    """
    Executes a bash command and returns both stdout and stderr.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip(), result.stderr.strip()

# Function to check if a command exists in the system
def command_exists(command):
    """
    Checks if a given bash command exists on the system.
    """
    result = subprocess.run(f'which {command}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0

# Function to execute a bash command without waiting for it to finish (asynchronous)
def execute_command_async(command):
    """
    Executes a bash command asynchronously without waiting for it to complete.
    """
    subprocess.Popen(command, shell=True)

# Function to capture the output of a command in real-time
def execute_command_realtime(command):
    """
    Executes a bash command and streams its output line by line in real-time.
    """
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line, end='')

# Function to get the exit code of a bash command
def get_command_exit_code(command):
    """
    Executes a bash command and returns its exit code.
    """
    result = subprocess.run(command, shell=True)
    return result.returncode

# Function to run a command with custom environment variables
def execute_command_with_env(command, env_vars):
    """
    Executes a bash command with custom environment variables.
    `env_vars` should be a dictionary of environment variables.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env_vars)
    return result.stdout.strip()

