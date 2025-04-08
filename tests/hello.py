from abp import *

key = "ABC123"
patterns = generate_patterns(key)
text = "Hello, World!"
encrypted = encode(text, patterns)
decrypted = decode(encrypted, patterns)
print("Encrypted :", encrypted)
print("Decrypted :", decrypted)
