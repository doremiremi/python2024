import qrcode

url = 'https://www.instagram.com/do____fasolatido/'
img = qrcode.make(url)
img.save('./remmi.png')