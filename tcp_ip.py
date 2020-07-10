import socket



def tcp_ip():
    
    while True:
        port_or_name = input('enter protocol name or port : ')
        try:
            protocol = int(port_or_name)   
            try:
                protocol = socket.getservbyport(protocol)
                print('the protocol with the port number of %s is  %s ' %(port_or_name,protocol ))
            
                
            except OSError as e:
                print(e)
                continue
            except OverflowError as o:
                print(o)
                continue
                   
        except ValueError as v:
            try:
                protocol = socket.getservbyname(port_or_name)
                print('the protocol port with the name of %s is %s  ' %(port_or_name, protocol))
            
                
            except OSError as e:
                print(e)
                continue
            
            continue
            
        

if __name__ == '__main__':
    tcp_ip()
