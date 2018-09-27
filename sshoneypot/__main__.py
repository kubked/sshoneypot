"""SSHoneypot is a simple SSH server serving rubbish for the clients

It works on port 22 by default and as now it can't be changed by environment
variable.
"""
import asyncio
import signal

from sshoneypot import keygen
from sshoneypot import server


DEFAULT_IP = '0.0.0.0'


# check if server private key exists
keygen.generate_unexisting_key()

# get event loop and assign handling SIGTERM stop message
loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGTERM, loop.stop)
loop.run_until_complete(server.create_server(DEFAULT_IP, 8822))

try:
    print("Running...")
    loop.run_forever()
except KeyboardInterrupt:
    print("Closing...")
    loop.close()
