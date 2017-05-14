FROM ubuntu:16.04
COPY d-apt.gpg.key /root/d-apt.gpg.key
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget
RUN wget http://master.dl.sourceforge.net/project/d-apt/files/d-apt.list -O /etc/apt/sources.list.d/d-apt.list
RUN apt-key add < /root/d-apt.gpg.key && apt-get update
RUN apt-get install -y dmd-bin dub libevent-dev libssl-dev inotify-tools vim postgresql libpq-dev python-psycopg2 python-numpy
RUN update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.gold" 20
RUN update-alternatives --install "/usr/bin/ld" "ld" "/usr/bin/ld.bfd" 10
ARG uid
RUN groupadd -g "$uid" user
RUN useradd -u "$uid" -g "$uid" -m user
RUN mkdir /db && chown "$uid" /db
USER "$uid"
RUN /usr/lib/postgresql/9.5/bin/initdb /db
RUN echo "unix_socket_directories = '/db'" >> /db/postgresql.conf
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/9.5/bin
ENV PGDATA=/db
ENV PGHOST=/db
ENV PGDATABASE=postgres
