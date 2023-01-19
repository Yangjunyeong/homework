def salt_function():

    salt_n,salt_g = [],[]
    for i in range(5):
    # input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
        salt = input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
        if  salt == "Done":
            break
        else:
            salt_s = list(map(str,salt.split()))
            s, sw = salt_s[0][:-1], salt_s[1][:-1]
            salt_n.append(float(s) / 100 * float(sw))
            salt_g.append(float(sw))

    return str(round(sum(salt_n) * 100 / sum(salt_g), 2)) + "%", str(round(sum(salt_g), 2)) + "g"

