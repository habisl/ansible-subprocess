import subprocess


def run_playbook(playbook_filename, hosts, playbook_cmd='ansible-playbook', private_key=None, extra_options=None, **extra_vars):

    command = construct_playbook_command(playbook_filename, hosts, playbook_cmd, private_key, extra_vars)

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def construct_playbook_command(playbook_filename, hosts, playbook_command='ansible-playbook', private_key=None, extra_options=None, extra_vars=None):

    if isinstance(hosts, list):
        hosts = ",".join(hosts) + ","

    if not isinstance(hosts, str):
        raise TypeError('hosts must be a str or list object')

    command = [
        playbook_command,
        playbook_filename,
        '-i',
        hosts,
    ]

    if extra_vars:
        vars = ' '.join("{}={}".format(key, value) for (key, value) in extra_vars.keys())
        command.extend(['--extra-vars', vars])

    if not extra_options:
        return command

    if isinstance(extra_options, str):
        command.append(extra_options)
    elif isinstance(extra_options, list):
        command.extend(extra_options)
    else:
        raise TypeError("extra_options must be str or list.")

    return command


def run_ping(host, ansible_command='ansible'):

    command = construct_ping_command(host, ansible_command=ansible_command)

    process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return (process.wait(), process.stdout.read(), process.stderr.read())


def construct_ping_command(host, ansible_command='ansible'):

    command = [
        ansible_command,
        host,
        '-m',
        'ping'
    ]

    return command
