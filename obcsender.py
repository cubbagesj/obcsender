#
# This program is part of the Autonomous Model Software Package
#
# obcsender.py - A program to read an obc file and recreate CB12 OBC data pkts
# This program needs to be modified whenever the CB12 packet map changes
#
# To use this program, the CB12 version of AM_Control needs to be modified
# to look for ADCP velocity in the Z_lin_accel channel and to manually
# set the script speed and depth
#

import socket, struct
import time

# Socket setup - send straight to Control computer
# which is running on frmpi1
#
addr = ("192.168.1.210", 3188)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.5)

# Define the OBC message formats
# This format has to change whenever the packet map changes
#
# CB12 splits the OBC data into two UDP packets
obcAfmt = '>HHL551xHdHdHd157x'
obcBfmt = '>394xHHHHhhhhhhhhhhhh320x'

# Read in the OBC file and then loop to send packets

obcfilename = 'run-1321.obc'

pktcnt = 0

obcfile = open(obcfilename, 'r')
for record in obcfile:
    record = record.rstrip()
    data = record.split()



    # Pack the data into the message
    # 
    # Message1 contains the depth gauges 
    # need to manually enter the depth gains
    message1 = struct.pack(obcAfmt, 
            0xf0c1,
#            int(data[1]),
            pktcnt,
            0,
            1,
            (float(data[11])*0.00178771),
            1,
            (float(data[12])*23.15228962),
            1,
            (float(data[13])*0.00176125))

    # LN200 and ADCP come in message 2
    # Putting ADCP xvel in z-lin-accel for now
    message2 = struct.pack(obcBfmt,
            1,
            0,
            0,
            0,
            int(float(data[246])),
            int(float(data[196])),
            int(float(data[197])),
            int(float(data[198])),
            int(float(data[199])),
            int(float(data[200])),
            int(float(data[201])),
            int(float(data[202])),
            int(float(data[203])),
            int(float(data[204])),
            int(float(data[205])),
            int(float(data[206])))


    print(float(data[220])*(.045))
    # Send the two OBC pkts
    s.sendto(message1, addr)
    s.sendto(message2, addr)

    pktcnt += 1
    # Wait to send next packet
    time.sleep(.01)


