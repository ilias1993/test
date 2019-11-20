import data

class firmware_data:
    
    def __init__(self, version, status, CRC, board, value, footer):
        self.version = version
        self.status = status
        self.CRC = CRC
        self.board = board
        self.value = value
        self.footer = footer

    def full_info(self):
        return "{} {} {} {} {} {}".format(self.version, self.status, self.CRC, self.board, self.value, self.footer)


firmware_1 = firmware_data("2.0.0", "update", "unverified", "card_1", 1, 0xFFFF)
print(firmware_1.version)
print(data.firmware["version"])
print(firmware_1.full_info())
