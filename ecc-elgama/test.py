from utils import modinv, decode_ascii, encode_ascii


# a = 16
# n = 138
# inv = modinv(a, n)
# print(inv)
# print(a * inv % n)

print(encode_ascii("TR"), decode_ascii(511))
