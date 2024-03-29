from binascii import a2b_hex, b2a_hex
import hashlib
import hmac

ssid = b"RAPPER"
passphrase = b"12345678"
apmac = a2b_hex("b827eb50ff9a")
smac = a2b_hex("10440082e7ef")
anonce = a2b_hex("820e0ebfd8bad560ca17f85097366328df40de0bc8a95782d7a5d0417d6df964")
snonce = a2b_hex("cb9f0fb38263fa529b4c5ac7a0a3c0c006e1a20a68370e86bad654b076550976")
message = b"".join(
    [
        b"Pairwise key expansion\x00",
        min(apmac, smac),
        max(apmac, smac),
        min(anonce, snonce),
        max(anonce, snonce),
        b"\x00",
    ]
)
payload = b"".join(
    [
        a2b_hex(
            "0103007502010a00000000000000000001cb9f0fb38263fa529b4c5ac7a0a3c0c006e1a20a68370e86bad654b0765509760000000000000000000000000000000000000000000000000000000000000000"
        ),
        bytearray(16),
        a2b_hex("001630140100000fac040100000fac040100000fac020000"),
    ]
)


pmk = hashlib.pbkdf2_hmac("sha1", passphrase, ssid, 4096, 32)
kck = hmac.new(pmk, message, hashlib.sha1).digest()[:16]
mic = hmac.new(kck, payload, hashlib.sha1).digest()[:16]

print(b2a_hex(mic))


# MIC 1: 02a5205d60db0558622eb678829ce1d4
# MIC 2: bc3aa944d84f34fa2dbc12fdac5a8c32
# MIC 3: 3037cf0bd15f777c466b7e0dd6211384
