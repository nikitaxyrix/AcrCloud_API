from ACR_API import init, recognize

init('###YOUR ACCESS KEY###', '###YOUR ACCESS SECRET###', False, 'Request URL (if you need it). Usually empty')
output = recognize('file.mp3')
print(output) # Output acrcloud result