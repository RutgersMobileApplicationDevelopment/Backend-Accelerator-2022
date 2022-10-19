from pyqrcode import create as QR

def main():
    url = input("URL: ")
    out = input("Destination: ")
    QR(url).png(out,scale=8)

if __name__ == "__main__":
    main()