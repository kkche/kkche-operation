
cd /tmp
wget http://www.redmine.org/releases/redmine-2.5.0.tar.gz
tar xfzv redmine-2.5.0.tar.gz
mv /tmp/redmine-2.5.0 ~/software
cd ~/software/redmine-2.5.0

mysql 
> create database redmine character set utf8;
> create user 'redmine'@'localhost' identified by '<password>';
> grant all privileges on redmine.* to 'redmine'@'localhost';
> flush privileges;

cp config/database.yml.example config/database.yml
vi config/database.yml

sudo apt-get install imagemagick libmagickwand-dev

vi Gemfile
source 'http://ruby.taobao.org'

sudo gem install bundler
bundle install --without development test

rake generate_secret_token

RAILS_ENV=production rake db:migrate
RAILS_ENV=production rake redmine:load_default_data

mkdir -p tmp tmp/pdf public/plugin_assets
sudo chown -R <user>:<group> files log tmp public/plugin_assets
sudo chmod -R 755 files log tmp public/plugin_assets

ruby script/rails server webrick -e production

http://localhost:3000/
login: admin
password: admin

cp config/configuration.yml.example config/configuration.yml
cp config/additional_environment.rb.example config/additional_environment.rb

mysqldump -u <username> -p<password> <redmine_database> | gzip > /path/to/backup/db/redmine_`date +%y_%m_%d`.gz

rsync -a /path/to/redmine/files /path/to/backup/files

sudo gem install unicorn

vi Gemfile

```
gem "unicorn", "4.8.3"
```

sudo vi /var/ubuntu/software/redmine-2.5.0/config/unicorn.rb

```
worker_processes 1
working_directory "/var/ubuntu/software/redmine-2.5.0"

listen "/tmp/redmine_unicorn.socket", :backlog => 64
pid "/tmp/redmine_unicorn.pid"

timeout 60

preload_app true

stderr_path "/var/ubuntu/software/redmine-2.5.0/log/redmine_unicorn_stderr.log"
stdout_path "/var/ubuntu/software/redmine-2.5.0/log/redmine_unicorn_stdout.log"

before_fork do |server, worker|
  defined?(ActiveRecord::Base) and ActiveRecord::Base.connection.disconnect!
end

after_fork do |server, worker|
  defined?(ActiveRecord::Base) and ActiveRecord::Base.establish_connection
  worker.user('ubuntu', 'sudo') if Process.euid == 0
end
```

sudo vi /etc/rc.local

```
bundle exec unicorn_rails -E production -c /var/ubuntu/software/redmine-2.5.0/config/unicorn.rb -D
```

sudo vi /etc/nginx/sites-available/redmine

```
upstream redmine_unicorn { 
    server unix:/tmp/redmine_unicorn.socket;
}

server {
    listen 0.0.0.0:80;
    server_name redmine.kkche.org;

    access_log /var/log/nginx/redmine_unicorn_access.log;
    error_log /var/log/nginx/redmine_unicorn_error.log;
 
    proxy_connect_timeout 60;
    proxy_read_timeout    60;
    proxy_send_timeout    60;

    location / {
      root /var/ubuntu/software/redmine-2.5.0/public;
      if (!-f $request_filename) { 
          break;
      }
      
      proxy_set_header X-Real-IP $remote_addr;
      proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
      proxy_set_header Host $http_host; 
      proxy_pass http://redmine_unicorn;
      proxy_redirect off; 
    }
 }
```

ln -s /etc/nginx/sites-available/redmine /etc/nginx/sites-enabled/redmine

