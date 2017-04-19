"""
__author__: surajshah
Adapted from surajshah assignment1 reflector sourcecode
"""
import argparse
from scapy.all import *
import sys
from scapy.layers.inet import IP
from scapy.layers.l2 import ARP, Ether
import pdb
import traceback

VICTIM_IP = ''
VICTIM_MAC = ''
REFLECTOR_IP = ''
REFLECTOR_MAC = ''
INTERFACE = ''
ATTACKER_IP = ''
ATTACKER_MAC = ''

def _parseArgs():
    parser = argparse.ArgumentParser(description='Arguments for the reflector...')
    parser.add_argument('--interface', help='example: eth0 | ens33', required=True)
    parser.add_argument('--victim-ip', help='Victim IP example: 192.168.1.10', type=str,required=True)
    parser.add_argument('--victim-ethernet', help='Victim MAC example: 31:16:A9:63:FF:83', required=True)
    parser.add_argument('--reflector-ip', help='Reflector-ip example: 192.168.1.20', required=True)
    parser.add_argument('--reflector-ethernet', help='Reflector MAC example: 38:45:E3:89:B5:56',required=True)
    return vars(parser.parse_args())

#This function is not being used
def arpPoisoning(src_mac, src_ip, tgt_ip, tgt_mac):
	"""
		Not used ... 1st poison the network into thinking you are the victim as well as the reflector
	"""
	#Here Ethernet layer will need to be changed too
	arp = ARP()
	arp.hwsrc = src_mac
	arp.psrc = src_ip
	arp.hwdst = tgt_mac
	arp.pdst = tgt_ip
	arp.op = ARP.who_has
	#sendp(arp, iface=INTERFACE)
	send(arp, iface=INTERFACE)

def reflector(pkt):
	"""
	reflect the packets back to attacker
	"""
	# pkt.summary()
	# pkt.command()
	#pkt = eval(oldpkt.command())
	global INTERFACE, VICTIM_IP, VICTIM_MAC, REFLECTOR_IP, REFLECTOR_MAC, ATTACKER_MAC, ATTACKER_IP
	try:
		if IP in pkt:
			del(pkt[IP].chksum)
			if pkt[IP].dst == VICTIM_IP:
				print ">>>>>>>>>Received an IP request on victim>>>>>>>"
				pkt.show()
				ATTACKER_IP = pkt[IP].src
				ATTACKER_MAC = pkt[Ether].src
				#arp poisoning
				#arpPoisoning(REFLECTOR_MAC, REFLECTOR_IP, ATTACKER_IP, ATTACKER_MAC)

				pkt[IP].dst = pkt[IP].src
				pkt[IP].src = REFLECTOR_IP
				#pkt[IP].ttl = 64
				
				#packet.show()
				pkt[Ether].dst = pkt[Ether].src
				pkt[Ether].src = REFLECTOR_MAC

				# newPkt = Ether(dst=pkt[Ether].src, src=REFLECTOR_MAC)/IP(dst=pkt[IP].src,src=REFLECTOR_IP,ttl=64,flags=pkt[IP].flags)
				# if TCP in pkt:
				# 	newPkt = newPkt / TCP(dport=pkt[TCP].sport,sport=pkt[TCP].dport)
				# elif UDP in pkt:
				# 	newPkt = newPkt / UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)
				# elif ICMP in pkt:
				# 	newPkt = newPkt / ICMP()
				# if Raw in pkt:
				# 	newPkt = newPkt / pkt[Raw]

				print ">>>>>>>>>New Packet>>>>>>>>>>>>>>"
				# newPkt.show()
				# sendp(newPkt)
				pkt.show()
				sendp(pkt, iface=INTERFACE)
				print ">>>>>>>>>Response from attacker>>>>>>>>>>>"
			
			elif pkt[IP].dst == REFLECTOR_IP:
				print ">>>>>>>>>Received an IP response on reflector>>>>>>>>>"
				pkt.show()
		  		pkt[IP].dst = pkt[IP].src
				pkt[IP].src = VICTIM_IP
				#pkt[IP].ttl = 64
				#packet.show()
				pkt[Ether].dst = pkt[Ether].src
				pkt[Ether].src = VICTIM_MAC
				pkt.show()
				sendp(pkt, iface=INTERFACE)


		elif ARP in pkt and pkt[ARP].op == 1 and pkt[ARP].pdst == VICTIM_IP:
			pkt[Ether].dst = pkt[Ether].src
			pkt[Ether].src = VICTIM_MAC
			pkt[ARP].hwsrc = VICTIM_MAC
			pkt[ARP].hwdst = pkt[Ether].dst
			pkt[ARP].pdst = pkt[ARP].psrc
			pkt[ARP].psrc = VICTIM_IP
			pkt[ARP].op = 2
			sendp(pkt, iface=INTERFACE)	
			print ">>>>>>>>>Received an arp request on victim>>>>>>>"
			pkt.show()			
		elif ARP in pkt and pkt[ARP].op == 1 and pkt[ARP].pdst == REFLECTOR_IP:
			pkt[Ether].dst = pkt[Ether].src
			pkt[Ether].src = REFLECTOR_MAC
			pkt[ARP].hwsrc = REFLECTOR_MAC
			pkt[ARP].hwdst = pkt[Ether].dst
			pkt[ARP].pdst = pkt[ARP].psrc
			pkt[ARP].psrc = REFLECTOR_IP
			pkt[ARP].op = 2
			sendp(pkt, iface=INTERFACE)	
			print ">>>>>>>>>Received an arp request reflector>>>>>>>"
			pkt.show()			
		else:
			print ">>>>\n>>>>>Packet not of our interest>>>\n>>>>>"
			pkt.show()
	except Exception as e:
		print "Exception in reflector:",e
		print traceback.format_exc()


def main():
	"""
		Scapy documentation referred
	"""
	try:
		#pdb.set_trace()
		#get commandline arguments
		val = _parseArgs()
		global INTERFACE, VICTIM_IP, VICTIM_MAC, REFLECTOR_IP, REFLECTOR_MAC
		INTERFACE = val['interface']
		VICTIM_IP = val['victim_ip']
		VICTIM_MAC = val['victim_ethernet']
		REFLECTOR_IP = val['reflector_ip']
		REFLECTOR_MAC = val['reflector_ethernet']

		#arp poisoning
		#arpPoisoning(VICTIM_MAC, VICTIM_IP)

		#sniff packets from the network at the specified interface
		#source: https://thepacketgeek.com/scapy-p-05-sending-our-first-packet-arp-response/

		pkts = sniff(count=100000,iface=INTERFACE,prn=reflector)

		# for pkt in pkts:
		# pkt = modifyPacket(pkt)

	except Exception as e:
		print "Exception in main: ",e

if __name__ == '__main__':
    main()