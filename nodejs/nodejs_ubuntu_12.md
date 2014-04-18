#nodejs在ubuntu server 12版本上的安装

	sudo apt-get install python-software-properties python g++ make
	sudo add-apt-repository ppa:chris-lea/node.js
	sudo apt-get update
	sudo apt-get install nodejs
	
不要 apt-get install npm，npm已经包含在nodejs包中，npm包中是老版本的软件，不要安装！！