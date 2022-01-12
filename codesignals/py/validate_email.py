def findEmailDomain(address):
    domain_start = address.rfind('@') +1
    return address[domain_start:]