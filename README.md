# AES 128-bit CTR
* Advanced Encryption Standard-128 CTR (Counter) is a mode of operation for the Advanced Encryption Standard (AES) algorithm. AES is a widely used symmetric encryption algorithm that provides secure and efficient encryption and decryption of data.

*In AES-128 CTR mode, the key is expanded into round keys, a counter value is initialized, and for each data block, the counter is encrypted to generate a keystream. The keystream is then XORed with the plaintext or ciphertext block to produce the encrypted or decrypted block. The counter value is incremented for the next block, and these steps are repeated until the entire message is processed.

*The main advantage of CTR mode is that it allows parallel encryption and decryption of blocks, making it efficient for both small and large data sets. It also provides random access to the ciphertext, as the encryption and decryption process does not require preceding blocks.

*The security of AES-128 CTR relies on the uniqueness of the counter values. Reusing the same counter value with the same key compromises the security of the encryption. It is crucial to use a unique nonce and/or block number for each encryption operation.

In conclusion, AES-128 CTR is a secure and efficient mode of operation for AES encryption, providing confidentiality for data transmission or storage.
