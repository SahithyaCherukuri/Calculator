For task3:
I have 4 microservices that run on the docker containers.

First step is to create the containers:
Got to each folder and create images as follows:
- cd Addition
- docker build -t plus_image .

- cd ../Subtraction
- docker build -t minus_image .

- cd ../Multiplication
- docker build -t multiply_image .

- cd ../Divide
- docker build -t divide_image .

After this, Follow these steps: (current directory .. Task4)

Run the command

- python app.py
- open the link given in the command line (Something like this: http://192.168.0.47:80/)
- now calculate the expressions (use space between each character)

Example: M + 5 * M / 4 - M
        2 + 3 - 4 * 7