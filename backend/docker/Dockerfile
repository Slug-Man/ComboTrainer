FROM ubuntu:16.04
COPY . /
RUN apt-get update
RUN apt-get install -y wget
RUN wget http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -O /etc/apt/sources.list.d/d-apt.list
RUN apt-key add < /d-apt.gpg.key && apt-get update
RUN apt-get install -y dmd-bin dub libevent-dev libssl-dev inotify-tools vim
RUN mkdir /.dub && chmod 777 /.dub
RUN update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 20
RUN update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.bfd" 10
