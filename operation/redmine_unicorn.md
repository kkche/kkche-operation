安装unicorn
	
	sudo gem install unicorn

编辑/var/ubuntu/software/redmine-2.5.0/config/unicorn.rb，内容为：

	#unicorn.rb Starts here
	worker_processes 1
	working_directory "/var/ubuntu/software/redmine-2.5.0" # needs to be the correct directory for redmine
	
	# This loads the application in the master process before forking
	# worker processes
	# Read more about it here:
	# http://unicorn.bogomips.org/Unicorn/Configurator.html
	preload_app true
	timeout 45

	# This is where we specify the socket.
	# We will point the upstream Nginx module to this socket later on
	listen "/tmp/unicorn_rails_redmine.socket", :backlog => 64 #directory structure needs to be created.
	pid "/var/ubuntu/software/redmine-2.5.0/tmp/pids/unicorn_rails.pid" # make sure 	this points to a valid directory. Make sure it is named the same as the real 	process name in order to allow init.d script start-stop-daemon command to kill 	unicorn process properly

	# Set the path of the log files inside the log folder of the testapp
	stderr_path "/var/ubuntu/software/redmine-2.5.0/log/unicorn_rails.stderr.log"
	stdout_path "/var/ubuntu/software/redmine-2.5.0/log/unicorn_rails.stdout.log"

	before_fork do |server, worker|
	# This option works in together with preload_app true setting
	# What is does is prevent the master process from holding
	# the database connection
	defined?(ActiveRecord::Base) and
	ActiveRecord::Base.connection.disconnect!
	end

	after_fork do |server, worker|
	# Here we are establishing the connection after forking worker
	# processes
	defined?(ActiveRecord::Base) and
	ActiveRecord::Base.establish_connection
	# change below if your redmine instance is running differently
	worker.user('ubuntu', 'sudo') if Process.euid == 0
	end
	#unicorn.rb Ends here

编辑/etc/rc.local，加入开机启动unicorn的脚本：

	/usr/local/bin/unicorn_rails -E production -c /usr/share/redmine/config/unicorn.rb -D

编辑/etc/nginx/sites-available/redmine

	upstream unicorn_server {
		# This is the socket we configured in unicorn.rb
		server unix://tmp/unicorn_rails_redmine.socket
		fail_timeout=0;
	}

	server {
		listen 0.0.0.0:80;
		server_name redmine.kkche.org ;
		access_log /var/log/nginx/redmine.log;

		# pass the request to the node.js server with the correct headers and much more can be added, see nginx config options
		location / {
			#proxy_set_header X-Real-IP $remote_addr;
			#proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			#proxy_set_header Host $http_host;
			#proxy_set_header X-NginX-Proxy true;
			proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
			proxy_set_header Host $http_host;
			proxy_redirect off;

			if (!-f $request_filename) {
				proxy_pass http://unicorn_server;
				break;
			}
		}
	}
	
让redmine配置在nginx里起作用：

	ln -s /etc/nginx/sites-available/redmine /etc/nginx/sites-enabled/redmine


