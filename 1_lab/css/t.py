def decode_hexstring(hexstring):
    decoded = ''

    for i in range(0, len(hexstring), 2):
        b = hexstring[i:i+2]
        b = b.decode()  # it's a byte-string

        try:
            c = bytes.fromhex(b).decode()
        except:  # the last char might be missing
            c = '☐'

        decoded = decoded + c

    return decoded


code = b'0201061a1695fe58585b05c2e525f438c1a4931282f13902000023c16c580b094c5957534430334d4d430000000000000000000000000000000000000000'
print(decode_hexstring(code))
