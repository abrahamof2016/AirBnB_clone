# AirBnB clone - The console


# Project Description

project to Deploy a simple copy of the AriBnB website on server.

# Console

Command interpreter to manage AirBnB Objects.

# How to start and use the console
The command interpreter can be run both interactively and non-interactively.
To run the console in non-interactive mode:
    pipe any command into execution of console.py on your shell.

```
echo "help" | ./console.py
(hbnb)
```
To run in interactive mode run:
    `./console.py`
    or
    `python3 console.py`

# examples
# Interactive mode
```
$ ./console.py
(hbnb) help

Documented commands:
    EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
# Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands:
    EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands:
    EOF  help  quit
(hbnb)
$
```
