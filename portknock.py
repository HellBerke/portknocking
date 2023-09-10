import socket
import time
import logging

# Hedef IP adresi ve Knock yapılacak portlar
hedef_ip = input("Hedef IP adresini girin: ")
knock_portlar = [int(port) for port in input("Knock yapmak için kullanılacak portları virgülle ayırarak girin: ").split(",")]

# Log dosyası ayarları
logging.basicConfig(filename='knock.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def knock_portlar_sırası(hedef_ip, portlar):
    knock_yapılan_portlar = []
    for port in portlar:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            try:
                s.connect((hedef_ip, port))
                print(f"Port {port} Knock yapıldı.")
                knock_yapılan_portlar.append(port)
                time.sleep(1)  # Bekleme süresi
            except Exception as e:
                print(f"Port {port} Knock yapılamadı: {e}")
            finally:
                s.close()

    return knock_yapılan_portlar

# Portları Knock yapma işlemini başlat
knock_yapılan_portlar = knock_portlar_sırası(hedef_ip, knock_portlar)

if knock_yapılan_portlar == knock_portlar:
    # Eğer doğrulama başarılıysa, gerçek hedef servise eriş
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((hedef_ip, 6000))  # Hedef port varsayılanı
            print("Erişim sağlandı!")
    except Exception as e:
        print(f"Erişim mümkün değil: {e}")
else:
    print("Doğrulama başarısız!")

# Loglama
logging.info(f"Knock yapılan portlar: {knock_yapılan_portlar}")
