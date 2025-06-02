with open ("server.log", "r") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())
