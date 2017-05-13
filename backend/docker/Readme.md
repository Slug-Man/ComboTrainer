Building the image:

```
sudo docker build -t dlang .
```

How I created the container (your user id is probably different):

```
sudo docker create -v /home/emanuel/proj/ComboTrainer:/project --ulimit nofile=1024:1024 --user 1000:1000 --name=combodev -it dlang /bin/bash
```

How I start it:

```
sudo docker start -ai combodev
cd project/backend
dub build --build=release # run this once to build dependencies
./autorebuild
```
