#!/usr/bin/python 


from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

class MyTopo( Topo ):
	
	def build(self):

		#Add layer1 switches
		s1 = self.addSwitch( 's1' ) 

		#Add layer2 switches
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )
		s5 = self.addSwitch( 's5' )

		#Add layer2 hosts
		h5 = self.addHost( 'h5' )
		h6 = self.addHost( 'h6' )
		h7 = self.addHost( 'h7' )
		h8 = self.addHost( 'h8' )

		#Add layer3 hosts
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		h4 = self.addHost( 'h4' )
		h9 = self.addHost( 'h9' )
		h10 = self.addHost( 'h10' )

		#Add switch-switch links
		self.addLink( s1, s2, bw = 30, delay= '87us', loss = 3 )
		self.addLink( s1, s3, bw = 35, delay= '48us', loss = 2 )
		self.addLink( s1, s4, bw = 38, delay= '76us', loss = 4 )
		self.addLink( s1, s5, bw = 40, delay= '52us', loss = 2 )
		
		#Add layer1-2 switch-host links
		self.addLink( s1, h5, bw = 22, delay= '3ms', loss = 9 )
		self.addLink( s1, h6, bw = 25, delay= '1ms', loss = 7 )
		self.addLink( s1, h7, bw = 18, delay= '4ms', loss = 6 )
		self.addLink( s1, h8, bw = 20, delay= '2ms', loss = 8 )
		
		#Add layer2-3 switch-host links
		self.addLink( s2, h1, bw = 14, delay= '5ms', loss = 13 )
		self.addLink( s2, h2, bw = 12, delay= '4ms', loss = 15 )
		self.addLink( s3, h3, bw = 15, delay= '3ms', loss = 8 )
		self.addLink( s3, h4, bw = 11, delay= '2ms', loss = 9 )
		self.addLink( s4, h9, bw = 30, delay= '7ms', loss = 12 )
		self.addLink( s5, h10, bw = 25, delay= '5ms', loss = 10 )

'''
Create and test a custom network
'''
def simpleTest():

	topo = MyTopo()
	# Create and manage a network with a OvS controller and use TCLink
	net = Mininet(
	    topo = topo, 
	    controller = OVSController,
	    link = TCLink)
	# Start a network
	net.start()
	# Test connectivity by trying to have all nodes ping each other
	print("Testing network connectivity")
	net.pingAll()
	# Dump every hosts's and switches's connections
	dumpNodeConnections(net.hosts)
	dumpNodeConnections(net.switches)
	# Stop a network
	CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
