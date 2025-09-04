import time
import tracemalloc
import xor_aes  # นำเข้าโมดูล aes ที่เขียนเอง
import xnor_aes  # นำเข้าโมดูล aes ที่เขียนเอง

def print_message_info(message, message_type):
    message_size_kb = len(message) / 1024
    message_length = len(message)
    print(f"{message_type} size: {message_size_kb:.6f} KB")
    print(f"{message_type} bytes: {message_length} bytes")

class pt:
	
	def necb_test(key, plain_text):
	   aes_instance = xnor_aes.AES(key)
	   
	   # Start measuring time and memory
	   tracemalloc.start()
	   start_time = time.time()
	   
	   cipher_text = aes_instance.encrypt_ecb(plain_text)
	   decrypted_text = aes_instance.decrypt_ecb(cipher_text)
	   
	   # Stop measuring time and memory
	   end_time = time.time()
	   current, peak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring encrypted time and memory
	   tracemalloc.start()
	   start_etime = time.time()
	   
	   cipher_text = aes_instance.encrypt_ecb(plain_text)
	   
	   # Stop measuring encrypted time and memory
	   end_etime = time.time()
	   ecurrent, epeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring decrypted time and memory
	   tracemalloc.start()
	   start_dtime = time.time()
	   
	   decrypted_text = aes_instance.decrypt_ecb(cipher_text)
	   
	   # Stop measuring decrypted time and memory
	   end_dtime = time.time()
	   dcurrent, dpeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	  
	   print(f"Execution time: {end_time - start_time} seconds")
	   print(f"Current memory usage: {current / 10**6} MB")
	   print(f"Peak memory usage: {peak / 10**6} MB")
	   print(f"Encrypted time: {end_etime - start_etime} seconds")
	   print(f"Current encrypted memory usage: {ecurrent / 10**6} MB")
	   print(f"Peak encrypted memory usage: {epeak / 10**6} MB")
	   print(f"Decrypted time: {end_dtime - start_dtime} seconds")
	   print(f"Current decrypted memory usage: {dcurrent / 10**6} MB")
	   print(f"Peak decrypted memory usage: {dpeak / 10**6} MB")
	   print("Decryption successful:", plain_text == decrypted_text)
	  
	   # แสดงข้อมูลขนาดคีย์และจำนวนรอบ
	   aes_instance.display_key_info()
	   	   
	   # Check message info
	   print_message_info(plain_text, "Plain Text")
	   
	   #aes_instance.display_padding_info(plain_text)
	
	def ctr_test(key, plain_text, iv):
	   aes_instance = xor_aes
	   
	   # Start measuring time and memory
	   tracemalloc.start()
	   start_time = time.time()
	   
	   cipher_text = aes_instance.AES(key).encrypt_ctr(plain_text, iv)
	   decrypted_text = aes_instance.AES(key).decrypt_ctr(cipher_text, iv)
	   
	   # Stop measuring time and memory
	   end_time = time.time()
	   current, peak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring encrypted time and memory
	   tracemalloc.start()
	   start_etime = time.time()
	   
	   cipher_text = aes_instance.AES(key).encrypt_ctr(plain_text, iv)
	   
	   # Stop measuring encrypted time and memory
	   end_etime = time.time()
	   ecurrent, epeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring decrypted time and memory
	   tracemalloc.start()
	   start_dtime = time.time()
	   
	   decrypted_text = aes_instance.AES(key).decrypt_ctr(cipher_text, iv)
	   
	   # Stop measuring decrypted time and memory
	   end_dtime = time.time()
	   dcurrent, dpeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   print(f"Execution time: {end_time - start_time} seconds")
	   print(f"Current memory usage: {current / 10**6} MB")
	   print(f"Peak memory usage: {peak / 10**6} MB")
	   print(f"Encrypted time: {end_etime - start_etime} seconds")
	   print(f"Current encrypted memory usage: {ecurrent / 10**6} MB")
	   print(f"Peak encrypted memory usage: {epeak / 10**6} MB")
	   print(f"Decrypted time: {end_dtime - start_dtime} seconds")
	   print(f"Current decrypted memory usage: {dcurrent / 10**6} MB")
	   print(f"Peak decrypted memory usage: {dpeak / 10**6} MB")
	   print("Decryption successful:", plain_text == decrypted_text)
	   
	   # แสดงข้อมูลขนาดคีย์และจำนวนรอบ
	   aes_instance.AES(key).display_key_info() 
	   
	   # Check message info
	   print_message_info(plain_text, "Plain Text")  
	
	
	def ecb_test(key, plain_text):
	   aes_instance = xor_aes.AES(key)
	   
	   # Start measuring time and memory
	   tracemalloc.start()
	   start_time = time.time()
	   
	   cipher_text = aes_instance.encrypt_ecb(plain_text)
	   decrypted_text = aes_instance.decrypt_ecb(cipher_text)
	   
	   # Stop measuring time and memory
	   end_time = time.time()
	   current, peak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring encrypted time and memory
	   tracemalloc.start()
	   start_etime = time.time()
	   
	   cipher_text = aes_instance.encrypt_ecb(plain_text)
	   
	   # Stop measuring encrypted time and memory
	   end_etime = time.time()
	   ecurrent, epeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	   
	   # Start measuring decrypted time and memory
	   tracemalloc.start()
	   start_dtime = time.time()
	   
	   decrypted_text = aes_instance.decrypt_ecb(cipher_text)
	   
	   # Stop measuring decrypted time and memory
	   end_dtime = time.time()
	   dcurrent, dpeak = tracemalloc.get_traced_memory()
	   tracemalloc.stop()
	  
	   print(f"Execution time: {end_time - start_time} seconds")
	   print(f"Current memory usage: {current / 10**6} MB")
	   print(f"Peak memory usage: {peak / 10**6} MB")
	   print(f"Encrypted time: {end_etime - start_etime} seconds")
	   print(f"Current encrypted memory usage: {ecurrent / 10**6} MB")
	   print(f"Peak encrypted memory usage: {epeak / 10**6} MB")
	   print(f"Decrypted time: {end_dtime - start_dtime} seconds")
	   print(f"Current decrypted memory usage: {dcurrent / 10**6} MB")
	   print(f"Peak decrypted memory usage: {dpeak / 10**6} MB")
	   print("Decryption successful:", plain_text == decrypted_text)
	  
	   # แสดงข้อมูลขนาดคีย์และจำนวนรอบ
	   aes_instance.display_key_info()
	   	   
	   # Check message info
	   print_message_info(plain_text, "Plain Text")   
