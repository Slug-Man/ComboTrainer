Building the image:

```
sudo docker build "--build-arg=uid=$(id -u)" -t dlang .
```

How I created the container (your user id is probably different):

```
sudo docker create -v /home/emanuel/proj/ComboTrainer:/project --ulimit nofile=1024:1024 --user "$(id -u):$(id -u)" --name=combodev -it dlang /bin/bash
```

How I start it:

```
sudo docker start -ai combodev
```

Setting up the database (inside the container):

```
pg_ctl start
cd /project/database
python rangecomboeval_test.py # This fills up the database
pg_ctl stop
```

Building dependencies:
```
dub build --build=release # run this once to build dependencies
```

Start the web server and auto rebuild:

```
cd project/backend
./autorebuild # This should also automatically start postgresql
```
