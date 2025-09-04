import mode_aes  # นำเข้าโมดูล aes ที่เขียนเอง

# Main function to demonstrate AES encryption and decryption with performance testing
if __name__ == "__main__":
    mode = input("Do you want to use ecb, necb or ctr mode?: ").lower()
    
    if mode == 'necb':
        mode_aes.mode.necb()
        
    elif mode == 'ecb':
        mode_aes.mode.ecb()
    	
    elif mode == 'ctr':
        mode_aes.mode.ctr()
     
    else:
        print("Invalid mode selected. Please choose 'ecb' for ECB mode, 'necb' for NECB mode or 'ctr' for CTR mode.")
