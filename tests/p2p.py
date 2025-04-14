from abp import *
import base64

alice_key = "AliceSecret123"
alice_private_patterns = generate_patterns(alice_key)
alice_public_patterns = [[255 - x for x in pattern] for pattern in alice_private_patterns]

bob_key = "BobSecret456"
bob_private_patterns = generate_patterns(bob_key)
bob_public_patterns = [[255 - x for x in pattern] for pattern in bob_private_patterns]

message = "Hello"

# Alice signe le message
signed = encode(message, alice_private_patterns)

# Encode en base64 pour rendre lisible et chiffrable
signed_b64 = base64.b64encode(signed)

# Chiffre avec la clé publique de Bob
encrypted = encode(signed_b64.decode(), bob_public_patterns)

# Bob reçoit et déchiffre
received_signed_b64 = decode(encrypted, bob_private_patterns)

# Décodage base64 pour retrouver les bytes signés
received_signed = base64.b64decode(received_signed_b64)

# Récupération du message d'origine via la clé publique d'Alice
received_original = decode(received_signed, alice_public_patterns)

print(received_original)  # "Hello"
