def prompt():
    x = input("What is the CIDR block? \nXYZ . XYZ . XYZ . XYZ / ")
    if type(int(x)) == int:
        x = int(x)
        return x
    else:
        prompt()

def calc(x):
    num_of_available_ip_addresses = (2 ** (32 - x)) - 2
    return num_of_available_ip_addresses

def format_output(num_of_available_ip_addresses):
    formatted_num_of_available_ip_addresses = format(num_of_available_ip_addresses, ",")
    result = print("# of available IPs: {num_of_available_ip_addresses}".format(num_of_available_ip_addresses=formatted_num_of_available_ip_addresses))
    return result

def main():
    print("Subnet Calculator: \n")
    input = prompt()
    num_of_available_ip_addresses = calc(input)
    return format_output(num_of_available_ip_addresses)

main()