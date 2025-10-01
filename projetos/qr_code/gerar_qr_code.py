import qrcode

data = 'https://sgpl.concord.net.br'
img = qrcode.make(data)

img.save('qrcode_sgpl.png')