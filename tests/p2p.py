from abp import encode, decode, generate_patterns
import base64

alice_key = "AliceSecret123"
alice_private_patterns = generate_patterns(alice_key)
alice_public_patterns = [[(-x) % 256 for x in pattern] for pattern in alice_private_patterns]

bob_key = "BobSecret456"
bob_private_patterns = generate_patterns(bob_key)
bob_public_patterns = [[(-x) % 256 for x in pattern] for pattern in bob_private_patterns]

message = "Hello"

signed = encode(message, alice_private_patterns)

signed_b64 = base64.b64encode(signed)

encrypted = encode(signed_b64.decode(), bob_public_patterns)

received_signed_b64 = decode(encrypted, bob_private_patterns, return_bytes=True)

#received_signed = base64.b64decode(received_signed_b64)

received_b64 = decode(received_signed_b64, alice_public_patterns, return_bytes=True)

received = base64.b64decode(received_b64)

print("Message received :", received)
