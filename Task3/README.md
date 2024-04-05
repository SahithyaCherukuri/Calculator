For task3:
I have 4 microservices that run on the docker containers.

First step is to create the containers:
Got to each folder and create images as follows:
- cd Addition
- docker build -t plus .

- cd ../Subtraction
- docker build -t minus .

- cd ../Multiplication
- docker build -t multiply .

- cd ../Divide
- docker build -t divide .

I use one volume to run as follows:

docker volume create myvolume
docker run -v myvolume:/data plus 3  # adds 3 to 0 (use data as that is used in code)
docker run -v myvolume:/data plus 6 # adds 3 to 6

docker run -v myvolume:/data minus 6 # subtracts 6 from 0
docker run -v myvolume:/data minus 3 # subtracts 3 from -6

docker run -v myvolume:/data multiply 2 # multiply 2 to 10
docker run -v myvolume:/data multiply 3 # multiply 3 to 20

docker run -v myvolume:/data divide 2 # divide 100 by 2
docker run -v myvolume:/data divide 2 # divide 50 by 2