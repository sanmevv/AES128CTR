# AES 128-bit CTR
Advanced Encryption Standard-128 CTR (Counter) is a mode of operation for the AES algorithm.
AES is a widely used symmetric encryption algorithm known for its security and efficiency.
AES-128 CTR mode involves expanding the key into round keys and initializing a counter value.
For each data block, the counter is encrypted to generate a keystream.
The keystream is XORed with the plaintext or ciphertext block to produce the encrypted or decrypted block.
The counter value is incremented for the next block, and the process is repeated until the entire message is processed.
CTR mode allows for parallel encryption and decryption of blocks, making it efficient for small and large data sets.
It also provides random access to the ciphertext without requiring preceding blocks.
The security of AES-128 CTR relies on the uniqueness of the counter values.
Reusing the same counter value with the same key compromises the encryption's security.
It is crucial to use a unique nonce and/or block number for each encryption operation.

In conclusion, AES-128 CTR is a secure and efficient mode of operation for AES encryption, providing confidentiality for data transmission or storage.
