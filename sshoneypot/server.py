import asyncssh
import asyncio

from drawille import Canvas

from sshoneypot import keygen


class SSHPlayerServer(asyncssh.SSHServer):
    @classmethod
    async def handle_client(cls, process):
        pos = 0, 0
        i = 0
        process.stdout.write('\e[8;50;100t')
        while i < 1000:
            c = Canvas()
            visible = False

            if b'' == await process.stdin.read(1):
                visible = True


            process.stdout.write('\033[2J')
            process.stdout.write("\033[?25l")

            if visible:
                for i in range(pos[0], pos[0] + 10):
                    for j in range(pos[1], pos[1] + 10):
                        c.set(i % 80 - 40, j % 60 - 30)

            process.stdout.write(c.frame(-40, -30, 40, 30))

            await asyncio.sleep(1. / 15)
            pos = pos[0] + 1, pos[1] + 1
            i += 1

        process.exit(0)

    def begin_auth(self, username):
        """Return False to not authenticate and allow everyone to connect"""
        return False


async def create_server(ip, port, loop=None):
    await asyncssh.create_server(
        SSHPlayerServer, ip, port,
        server_host_keys=[keygen.KEY_PATH],
        process_factory=SSHPlayerServer.handle_client,
        loop=loop,
    )
