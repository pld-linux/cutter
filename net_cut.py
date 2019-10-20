#!/usr/bin/env python

import NetfilterQueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR)
        print(scapy_packet.show())
    packet.drop()

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="q", help="Enter the queue to be used for trapping values")
    options = parser.parse_args()[0]

    if not options.ip_range:
        parser.error("[-]please specify the iptables queue, use --help for more info")

    return options.q

queuenum=get_arguments()
queue = NetfilterQueue.NetfilterQueue()
queue.bind(queuenum, process_packet)
queue.run()