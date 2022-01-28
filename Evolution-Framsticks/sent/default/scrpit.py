with open("default.log", 'r') as f:
    for i in range(11):
        with open(f"default-{i}.log", 'w') as ff:
                for line in f:
                    ff.write(line)
                    if line.startswith('--------------------------------------------------'):
                        break
