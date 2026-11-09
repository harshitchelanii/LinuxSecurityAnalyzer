failed_attempts = 0
ip_attempts = {}

with open("sample_logs/auth.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            failed_attempts += 1
            parts = line.split()
            ip_address = parts[10]

            if ip_address in ip_attempts:
                ip_attempts[ip_address] += 1
            else:
                ip_attempts[ip_address] = 1

    for ip, attempts in ip_attempts.items():
        if attempts >= 2:
            print(f"Suspicious IP addresses with multiple failed attempts: {ip}")

print(ip_attempts)
print(f"Total failed attempts: {failed_attempts}")
