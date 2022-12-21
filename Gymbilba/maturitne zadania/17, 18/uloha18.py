with open("sifro.txt") as sifro, open("frekv.txt") as frekv:
    sifro_dump = "".join(sifro.readlines())
    
    o_freq_dict = {}
    
    for pair in frekv.readlines():
        if pair[0] != " ":
            pair = pair.split(" ")
        else:
            pair = [" ", pair.split(" ")[-1]]
        o_freq_dict[pair[0]] = int(pair[1])
    
    freq_dict = {}
    for char in "".join(sifro_dump.split("\n")):
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    
    o_freq_dict = dict([(val, key) for key, val in o_freq_dict.items()])
    print(o_freq_dict)
    print(freq_dict)
    desifr = []
    for line in sifro_dump.split("\n"):
        desifr_line = ""
        for char in line:
            desifr_line += o_freq_dict[freq_dict[char]]
        desifr.append(desifr_line)

    print("\n".join(desifr))
    out_file = open("kluc.txt", "w")
    out_file.write(str(freq_dict))