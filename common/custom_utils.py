from base64 import b64encode, b64decode
import asyncio
import socket
from hashlib import sha256
from string import ascii_letters, digits
from secrets import choice


def to_b64str(filename):
    try:
        with open(filename, 'rb') as image_file:
            encoded_string = b64encode(image_file.read()).decode('ascii')
            return encoded_string
    except IOError:
        print(f'something went wrong while reading the {filename} file')


def b64str_to_file(b64str, filepath):
    try:
        with open(filepath, 'wb') as b:
            b.writelines(b64decode(b64str))
    except IOError:
        print(f'something went wrong while processing {filepath}')
    except OSError:
        print(f'something went wrong while processing {filepath}')
    except BaseException:
        print(f'something went wrong while processing {filepath}')


# Usage: asyncio.run(wait_for_data())
async def wait_for_data():
    try:
        # Get a reference to the current event loop because
        # we want to access low-level APIs.
        loop = asyncio.get_running_loop()

        # Create a pair of connected sockets.
        rsock, wsock = socket.socketpair()

        # Register the open socket to wait for data.
        reader, writer = await asyncio.open_connection(sock=rsock)

        # Simulate the reception of data from the network
        loop.call_soon(wsock.send, 'abc'.encode())

        # Wait for data
        data = await reader.read(100)

        # Got data, we are done: close the socket
        print("Received:", data.decode())
        writer.close()

        # Close the second socket
        wsock.close()
    except BaseException:
        print(f'something went wrong while processing socket connection')


def set_password(value):
    return sha256(value)


def generate_password(length=8):
    alphabet = ascii_letters + digits
    password = ''.join(choice(alphabet) for i in range(length))
    return password
