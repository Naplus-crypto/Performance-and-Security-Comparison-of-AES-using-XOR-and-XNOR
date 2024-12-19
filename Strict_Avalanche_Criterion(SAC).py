import matplotlib.pyplot as plt
import aes, Xaes # นำเข้าโมดูล aes ที่เขียนเอง
import binascii
import os

def encrypt_aes(key, data):
    cipher = aes.AES(key).encrypt_ecb(data)
    return cipher
    
def encrypt_modified_aes(key, data):
    cipher = Xaes.AES(key).encrypt_ecb(data)
    return cipher

def bytes_to_bitstring(byte_data):
    return ''.join(f'{byte:08b}' for byte in byte_data)

def count_different_bits(bitstring1, bitstring2):
    return sum(bit1 != bit2 for bit1, bit2 in zip(bitstring1, bitstring2))
    
def mean(values):
    return sum(values) / len(values)
         
def standard_deviation(values, mean_value):
    variance = sum((x - mean_value) ** 2 for x in values) / len(values)
    return variance ** 0.5
    
def rms_error(values):
    variance = sum((x - 64) ** 2 for x in values)
    return (variance ** 0.5) / len(values)
  
def test_sac(encrypt_function, original_data, key):
    # Encrypt the original data
    original_encrypted = encrypt_function(key, original_data)
    original_encrypted_bits = bytes_to_bitstring(original_encrypted)
    
    # Test all bits in the original data
    bit_changes = []
    for i in range(len(original_data) * 8):
        # Flip the i-th bit in the original data
        modified_data = bytearray(original_data)
        byte_index = i // 8
        bit_index = i % 8
        modified_data[byte_index] ^= 1 << bit_index
        
        # Encrypt the modified data
        modified_encrypted = encrypt_function(key, bytes(modified_data))
        modified_encrypted_bits = bytes_to_bitstring(modified_encrypted)
        
        # Count the number of different bits
        different_bits = count_different_bits(original_encrypted_bits, modified_encrypted_bits)
        bit_changes.append(different_bits)
        
        avg_changes = mean(bit_changes)
        std_dev_changes = standard_deviation(bit_changes, avg_changes)
        rms_error_changes = rms_error(bit_changes)
    
    return bit_changes, avg_changes, std_dev_changes, rms_error_changes

# Example usage
key = os.urandom(16)
original_data = os.urandom(16)

# Test original AES
print("Testing original AES...")
bit_changes_original, avg_changes_original, std_dev_changes_original,rms_error_changes_original = test_sac(encrypt_aes, original_data, key)
print(f"Original AES - Average number of bit changes per test: {avg_changes_original}")
print(f"Original AES - Standard deviation of bit changes per test: {std_dev_changes_original}")
print(f"Original AES - RMSE of bit changes per test: {rms_error_changes_original}")
print(f"Original AES - Bit changes from each test: {bit_changes_original}")
    
# Test modified AES
print("Testing modified AES...")
bit_changes_modified, avg_changes_modified, std_dev_changes_modified, rms_error_changes_modified = test_sac(encrypt_modified_aes, original_data, key)
print(f"Modified AES - Average number of bit changes per test: {avg_changes_modified}")
print(f"Modified AES - Standard deviation of bit changes per test: {std_dev_changes_modified}")
print(f"Original AES - RMSE of bit changes per test: {rms_error_changes_modified}")
print(f"Modified AES - Bit changes from each test: {bit_changes_modified}")

# Create scatter plots
plt.figure(figsize=(14, 6))
    
# Plot for original AES
plt.subplot(1, 2, 1)
plt.scatter(range(len(bit_changes_original)), bit_changes_original, color='blue')
plt.title('Original AES - Bit Changes')
plt.xlabel('Test Number')
plt.ylabel('Number of Bit Changes')
plt.ylim(38,90)
plt.grid(True)
    
 # Plot for modified AES
plt.subplot(1, 2, 2)
plt.scatter(range(len(bit_changes_modified)), bit_changes_modified, color='green')
plt.title('Modified AES - Bit Changes')
plt.xlabel('Test Number')
plt.ylabel('Number of Bit Changes')
plt.ylim(38,90)
plt.grid(True)
    
# Show the plots
plt.tight_layout()
plt.show()
