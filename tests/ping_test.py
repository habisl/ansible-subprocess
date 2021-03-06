import unittest
from ansible_subprocess.main import construct_ping_command, run_ping


class PingCommandTest(unittest.TestCase):

    def test_construct_ping_command(self):
        command = construct_ping_command('8.8.8.8')
        self.assertEqual(
            command,
            [
                'ansible',
                'all',
                '8.8.8.8',
                '-m',
                'ping'
                ]
        )

    def test_construct_ping_command_with_specific_ansible_command(self):
        command = construct_ping_command('8.8.8.8', ansible_command='/bin/ansible')
        self.assertEqual(
            command,
            [
                '/bin/ansible',
                'all',
                '8.8.8.8',
                '-m',
                'ping'
                ]
        )
