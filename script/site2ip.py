import socket

input_file = input("Enter the path to the input file: ")
output_file = input("Enter the path to the output file: ")


with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
   for domain in input_f:
       domain = domain.strip()  
       try:
           ip_address = socket.gethostbyname(domain)
           output_f.write(f"{domain} -> {ip_address}\n")
       except socket.gaierror:
           output_f.write(f"{domain} -> NOT FOUND\n")

print("Domain to IP mappings saved to", output_file)

with open(input_file, "r") as input_f, open("onlyip.txt", "w") as output_f:
   for domain in input_f:
       domain = domain.strip()  
       try:
           ip_address = socket.gethostbyname(domain)
           output_f.write(f"{ip_address}\n")
       except socket.gaierror:
           pass

print("OnlyIP is also saved")
