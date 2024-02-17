def bucode_Sil(string):
    
    girdi = string
    
    i = 0

    while i < len(girdi):
       
        if girdi[i:i+6] == "BUCODE":   
            girdi = girdi[:i] + girdi[i+6:]
        else:     
            i += 1
    
    if not girdi:
        return print("UTKU")
        
    else:
        return print(girdi)

giris = input()
bucode_Sil(giris)



