import subprocess

def run_naabu(ip):
    # Construct the naabu command
    command = f"echo {ip} | naabu -nmap-cli 'nmap -sV'"
    
    # Execute the command using subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Capture the output and error, if any
    stdout, stderr = process.communicate()
    
    # Print the output and error
    print(stdout.decode('utf-8'))
    if stderr:
        print(stderr.decode('utf-8'))

def main():
    # Path to the text file containing IP addresses or URLs
    ip_file_path = '/home/kobe/Desktop/judge/alive.txt'
    
    # Open the file and read each line (IP address or URL)
    with open(ip_file_path, 'r') as file:
        for line in file:
            # Strip whitespace and newlines from the line
            line = line.strip()
            
            # Remove 'https://' and 'http://' prefixes if present
            if line.startswith("https://"):
                ip = line[len("https://"):]
            elif line.startswith("http://"):
                ip = line[len("http://"):]
            else:
                ip = line  # No prefix found, use the line as is
            
            # Run naabu against the IP address
            run_naabu(ip)

if __name__ == '__main__':
    main()
