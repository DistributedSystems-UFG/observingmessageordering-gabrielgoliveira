#To Do: Replace all this with a naming service

# With local addresses (within the same cloud region)
#PEERS = ['172.31.78.41','172.31.65.227','172.31.74.212','172.31.75.17','172.31.72.48','172.31.75.162']

# With public addresses (in the same region of the cloud)
# The last one is not fixed and must be changed each time the lab is restarted.
PEERS_SAME_REGION = ["100.25.72.80", "23.23.123.132", "34.235.105.7", "50.17.58.135", "54.209.66.27", "54.144.141.73"]

# With public addresses (in two separate regions - last two servers in Oregon)
PEERS_TWO_REGIONS = ["100.25.72.80", "23.23.123.132", "34.235.105.7", "50.17.58.135",  "52.25.8.115", "52.41.8.222"]


PEER_UDP_PORT = 4567
PEER_TCP_PORT = 5679
N = 6   # Number of peers
SERVER_ADDR ='54.144.141.73'
SERVER_PORT = 5678

