import socket

input_file_path = input("Enter the path to the input file: ")
output_file_path = input("Enter the path to save the output file: ")

with open(input_file_path, 'r') as input_file:
    domains = input_file.readlines()

results = {}
for domain in domains:
    domain = domain.strip()
    try:
        ip = socket.gethostbyname(domain)
        results[domain] = ip
    except socket.gaierror:
        results[domain] = "Could not resolve"

with open(output_file_path, 'w') as output_file:
    for domain, ip in results.items():
        output_file.write(f"{ip}\n")

print(f"Results saved to {output_file_path}")