FROM node:5.3.0

RUN rm -rf /opt/docker
RUN mkdir -p /opt/docker/
WORKDIR /opt/docker/

#RUN mkdir ~/.node-gyp
#COPY node-v5.3.0-headers.tar.gz /opt/docker/
#RUN tar zxf /opt/docker/node-v5.3.0-headers.tar.gz -C ~/.node-gyp && mv ~/.node-gyp/node-v5.3.0 ~/.node-gyp/5.3.0
#RUN cd /root/.node-gyp/5.3.0 && printf "9\n" > /root/.node-gyp/5.3.0/installVersion

ENV npm_config_loglevel verbose

RUN npm --registry=http://r.cnpmjs.org/ install -g pm2@latest

RUN npm --registry=http://r.cnpmjs.org/ install --production
RUN npm remove pinyin
RUN npm --registry=http://r.cnpmjs.org/ install pinyin
