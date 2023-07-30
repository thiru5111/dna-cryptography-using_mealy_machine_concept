'''
email_mac = email + mac
    #print(email_mac)

    # merging email and mac
    nums = []
    for i in email_mac:
        if i != '-':
            nums.append(ord(i))
    #print("ascii value for email+mac is")
    #print(nums)

    # getting pan
    nums1 = []

    for i in pan:
        nums1.append(ord(i))
    #print("ascii value for pan is")
    #print(nums1)

    key = []

    # merging of ascii values of email+mac+pan
    def zigzagTraversal(arr1: list, arr2: list) -> list:
        # Size of array 'ARR1' and 'ARR2'.
        n = len(arr1)
        m = len(arr2)

        result = [0] * (n + m)
        p, q = 0, 0

        # Zigzag traversal of array using pointers 'p' and 'q'.
        for i in range(n + m):
            if (p == n):
                result[i] = arr2[q]
                q += 1
            elif (q == m):
                result[i] = arr1[p]
                p += 1
            else:
                if (i % 2 == 0):
                    result[i] = arr1[p]
                    p += 1
                else:
                    result[i] = arr2[q]
                    q += 1

        return result

    array = zigzagTraversal(nums1, nums)
    #print("array", array)

    # conversion of ascci to binary
    def dectobin(array: list) -> list:
        array1 = []
        for i in array:
            array1.append(bin(i).replace("b", ""))
        return array1

    key = dectobin(array)
    #print("the generated key is")

    def tostring(key: list) -> str:
        str1 = ''
        for i in key:
            str1 += i
        return str1

    final_key = ''
    final_key = tostring(key)
    #print(final_key)

    # rask
    def rask(final_key: str) -> str:
      str2 = ''
      if len(final_key)<256:
        for i in range(0, (256 - len(final_key))):
            str2 += "0"
        str2 += final_key
      else:
          for i in range(0,256):
              str2+=final_key[i]
      return str2

    str3 = ''
    #print("final", len(final_key))
    str3 = rask(final_key)
    #print("generated rask is")
    #print("str3", len(str3))
    #print("key", len(str3))
    print(str3)
    return str3

'''
def zigzag_model(em,pn):
    z = []
    for i in range(len(em)):
        if i < len(pn):
            z.append(pn[i])
        if i < len(em):
            z.append(em[i])
    return z

def rask_trun(bn):
    if len(bn)>=256:
        rask = bn[:256]
    else:
        rask=bn
        for i in range(0,256-len(bn)):
            rask="0"+rask
    return rask

def binary_convert(z):
    bn = ""
    for i in z:
        bn += bin(i)[2:].zfill(8)
    return bn

def ascci_value(em):
    for i in range(len(em)):
        em[i]=ord(em[i])
    return em


def email_mac(email,mac):
    email_mac=email+mac
    email_mac=email_mac.replace("-","")
    return email_mac

def Key_Generation(email,mac,pan):

    emailmac=email_mac(email,mac)
    emailmac=list(emailmac)
    panid=list(pan)
    emailmac=ascci_value(emailmac)
    panid= ascci_value(panid)
    zigzag=zigzag_model(emailmac,panid)

    binary=binary_convert(zigzag)

    rask=rask_trun(binary)

    return rask







#Key_Generation("abcdefgh@gmail.com","0a-12-22-b4-99-66","aeypp8436r")