import struct

from mysql_mimic.errors import MysqlError, ErrorCode
from mysql_mimic.types import uint_3, uint_1
from mysql_mimic.utils import seq


class ConnectionClosed(Exception):
    pass


class MysqlStream:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.seq = seq(256)

    async def read(self):
        data = b""
        while True:
            header = await self.reader.read(4)

            if not header:
                raise ConnectionClosed()

            i = struct.unpack("<I", header)[0]
            payload_length = i & 0x00FFFFFF
            sequence_id = (i & 0xFF000000) >> 24

            expected = next(self.seq)
            if sequence_id != expected:
                raise MysqlError(
                    f"Expected seq({expected}) got seq({sequence_id})",
                    ErrorCode.MALFORMED_PACKET,
                )

            if payload_length == 0:
                return data

            data += await self.reader.read(payload_length)

            if payload_length < 0xFFFFFF:
                return data

    async def write(self, data):
        while True:
            # Grab first 0xFFFFFF bytes to send
            payload = data[:0xFFFFFF]
            data = data[0xFFFFFF:]

            payload_length = uint_3(len(payload))
            sequence_id = uint_1(next(self.seq))

            self.writer.write(payload_length + sequence_id + payload)
            await self.writer.drain()

            # We are done unless len(send) == 0xFFFFFF
            if len(payload) != 0xFFFFFF:
                return

    def reset_seq(self):
        self.seq.reset()
