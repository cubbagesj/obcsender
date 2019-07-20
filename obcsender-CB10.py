#
# This program is part of the Autonomous Model Software Package
#
# obcsender-CB10.py - A program to read an obc file and recreate CB10 OBC data pkts
#
#

import socket, struct
import time
from argparse import ArgumentParser

# Set up command line parser
#
parser = ArgumentParser()
parser.add_argument("filename",
        help="OBC file to send")

args = parser.parse_args()

# Socket setup - send straight to Control computer
# which is running on frmpi6
#
addr = ("192.168.1.210", 4950)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.5)

# Define the OBC message formats
#
# Start with just a blank packet with the type set
obcfmt = '<2HL2HLH h2LH32h h2LH128h h2LHLHLHhl6h h2LH12h4H h2LH18h 92x h2LH5x4h  149x'

# Read in the OBC file and then loop to send packets

obcfilename = args.filename

print("Sending file: %s" % obcfilename)

pktcnt = 0

obcfile = open(obcfilename, 'r')
for record in obcfile:
    record = record.rstrip()
    data = record.split()



    # Pack the data into the message
    # Mapping each channel - Can override a channel if needed
    # 
    message1 = struct.pack(obcfmt, 
            int(float(data[0])),
            int(float(data[1])),
            int(float(data[2])),
            int(float(data[3])),
            int(float(data[4])),
            int(float(data[5])),
            int(float(data[6])),
            int(float(data[7])),
            int(float(data[8])),
            int(float(data[9])),

            int(float(data[10])),
            int(float(data[11])),
            int(float(data[12])),
            int(float(data[13])),
            int(float(data[14])),
            int(float(data[15])),
            int(float(data[16])),
            int(float(data[17])),
            int(float(data[18])),
            int(float(data[19])),

            int(float(data[20])),
            int(float(data[21])),
            int(float(data[22])),
            int(float(data[23])),
            int(float(data[24])),
            int(float(data[25])),
            int(float(data[26])),
            int(float(data[27])),
            int(float(data[28])),
            int(float(data[29])),
            
            int(float(data[30])),
            int(float(data[31])),
            int(float(data[32])),
            int(float(data[33])),
            int(float(data[34])),
            int(float(data[35])),
            int(float(data[36])),
            int(float(data[37])),
            int(float(data[38])),
            int(float(data[39])),
            
            int(float(data[40])),
            int(float(data[41])),
            int(float(data[42])),
            int(float(data[43])),
            int(float(data[44])),
            int(float(data[45])),
            int(float(data[46])),
            int(float(data[47])),
            int(float(data[48])),
            int(float(data[49])),
            
            int(float(data[50])),
            int(float(data[51])),
            int(float(data[52])),
            int(float(data[53])),
            int(float(data[54])),
            int(float(data[55])),
            int(float(data[56])),
            int(float(data[57])),
            int(float(data[58])),
            int(float(data[59])),
            
            int(float(data[60])),
            int(float(data[61])),
            int(float(data[62])),
            int(float(data[63])),
            int(float(data[64])),
            int(float(data[65])),
            int(float(data[66])),
            int(float(data[67])),
            int(float(data[68])),
            int(float(data[69])),
            
            int(float(data[70])),
            int(float(data[71])),
            int(float(data[72])),
            int(float(data[73])),
            int(float(data[74])),
            int(float(data[75])),
            int(float(data[76])),
            int(float(data[77])),
            int(float(data[78])),
            int(float(data[79])),
            
            int(float(data[80])),
            int(float(data[81])),
            int(float(data[82])),
            int(float(data[83])),
            int(float(data[84])),
            int(float(data[85])),
            int(float(data[86])),
            int(float(data[87])),
            int(float(data[88])),
            int(float(data[89])),
            
            int(float(data[90])),
            int(float(data[91])),
            int(float(data[92])),
            int(float(data[93])),
            int(float(data[94])),
            int(float(data[95])),
            int(float(data[96])),
            int(float(data[97])),
            int(float(data[98])),
            int(float(data[99])),
            
            int(float(data[100])),
            int(float(data[101])),
            int(float(data[102])),
            int(float(data[103])),
            int(float(data[104])),
            int(float(data[105])),
            int(float(data[106])),
            int(float(data[107])),
            int(float(data[108])),
            int(float(data[109])),
            
            int(float(data[110])),
            int(float(data[111])),
            int(float(data[112])),
            int(float(data[113])),
            int(float(data[114])),
            int(float(data[115])),
            int(float(data[116])),
            int(float(data[117])),
            int(float(data[118])),
            int(float(data[119])),
            
            int(float(data[120])),
            int(float(data[121])),
            int(float(data[122])),
            int(float(data[123])),
            int(float(data[124])),
            int(float(data[125])),
            int(float(data[126])),
            int(float(data[127])),
            int(float(data[128])),
            int(float(data[129])),
            
            int(float(data[130])),
            int(float(data[131])),
            int(float(data[132])),
            int(float(data[133])),
            int(float(data[134])),
            int(float(data[135])),
            int(float(data[136])),
            int(float(data[137])),
            int(float(data[138])),
            int(float(data[139])),
            
            int(float(data[140])),
            int(float(data[141])),
            int(float(data[142])),
            int(float(data[143])),
            int(float(data[144])),
            int(float(data[145])),
            int(float(data[146])),
            int(float(data[147])),
            int(float(data[148])),
            int(float(data[149])),
            
            int(float(data[150])),
            int(float(data[151])),
            int(float(data[152])),
            int(float(data[153])),
            int(float(data[154])),
            int(float(data[155])),
            int(float(data[156])),
            int(float(data[157])),
            int(float(data[158])),
            int(float(data[159])),
            
            int(float(data[160])),
            int(float(data[161])),
            int(float(data[162])),
            int(float(data[163])),
            int(float(data[164])),
            int(float(data[165])),
            int(float(data[166])),
            int(float(data[167])),
            int(float(data[168])),
            int(float(data[169])),
            
            int(float(data[170])),
            int(float(data[171])),
            int(float(data[172])),
            int(float(data[173])),
            int(float(data[174])),
            int(float(data[175])),
            int(float(data[176])),
            int(float(data[177])),
            int(float(data[178])),
            int(float(data[179])),
            
            int(float(data[180])),
            int(float(data[181])),
            int(float(data[182])),
            int(float(data[183])),
            int(float(data[184])),
            int(float(data[185])),
            int(float(data[186])),
            int(float(data[187])),
            int(float(data[188])),
            int(float(data[189])),
            
            int(float(data[190])),
            int(float(data[191])),
            int(float(data[192])),
            int(float(data[193])),
            int(float(data[194])),
            int(float(data[195])),
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
            int(float(data[206])),
            int(float(data[207])),
            int(float(data[208])),
            int(float(data[209])),

            int(float(data[210])),
            int(float(data[211])),
            int(float(data[212])),
            int(float(data[213])),
            int(float(data[214])),
            int(float(data[215])),
            int(float(data[216])),
            int(float(data[217])),
            int(float(data[218])),
            int(float(data[219])),

            int(float(data[220])),
            int(float(data[221])),
            int(float(data[222])),
            int(float(data[223])),
            int(float(data[224])),
            int(float(data[225])),
            int(float(data[226])),
            int(float(data[227])),
            int(float(data[228])),
            int(float(data[229])),

            int(float(data[230])),
            int(float(data[231])),
            int(float(data[232])),


            int(float(data[238])),
            int(float(data[239])),
            int(float(data[240])),
            int(float(data[241])),
            int(float(data[247])),
            int(float(data[246])),
            int(float(data[248])),
            int(float(data[249])))

    # Send the OBC pkts
    s.sendto(message1, addr)

    pktcnt += 1
    # Wait to send next packet
    time.sleep(.01)


