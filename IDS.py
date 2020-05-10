from scapy.all import *


def sniff_batch_arp_packets(self, batch_size, batch_timeout):
    packets = []
    sniffed_packets = sniff(filter='arp', count=batch_size, timeout=batch_timeout, store=1)
    for sniffed_packet in sniffed_packets:
        packet = {
            'op': None,
            'hw_src': None,
            'ip_src': None,
            'ip_dst': None
        }
        if sniffed_packet[ARP].op == 1:
            packet['op'] = 'ARP_REQ'
        elif sniffed_packet[ARP].op == 2:
            packet['op'] = 'ARP_REP'
        packet['hw_src'] = self.scrub_address('hw', sniffed_packet.sprintf('%ARP.hwsrc%'))
        packet['ip_src'] = self.scrub_address('ip', sniffed_packet.sprintf('%ARP.psrc%'))
        packet['ip_dst'] = self.scrub_address('ip', sniffed_packet.sprintf('%ARP.pdst%'))
        packets.append(packet)
    return packets