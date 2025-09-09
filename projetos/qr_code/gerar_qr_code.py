import qrcode

data = 'https://concord.net.br'
img = qrcode.make(data)

img.save('qrcode_concordnet.png')