# 0x00. AirBnB clone - The console

![alt text](https://i.kinja-img.com/gawker-media/image/upload/s--oqmQXcZx--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/n0uxpip8onijaufkntu9.jpg)

### Description
First step in the creation of an AirBnB  clone

Building of the console:
* Base data model
* Command line interpreter
* Storage Engine

### Useful Concepts
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

----------------------
### Usage
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
And in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) $

```
### The command line interpreter (The Console)
These are the command line commands:
To run the console: `./console.py`

| Command                                                      | Description                             |
|:------------------------------------------------------------ |:---------------------------------------                       
| `quit`                                                       | Quits the console                       |
| `help`                                                       | Help documentation for command          |
| `create <class>`                                             | create an object and print its id       |
| `all` or `all <class>`                                       | shows all objects in stack              |
| `show <class> <id>` or `<class>.show(<id>)`                  | show a specified object                 |
| `destroy <class> <id>` or `<class>.destroy(<id>)`            | remove an object                        |
| `update <class> <id> <attribute name> "<attribute value>"`   | update an attribute of an object        |

### Storage Engine
The storage type used for this project is file storage. We implement this in the file: `file_storage.py`
Data flow:
`<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>`
      
### [1. Be PEP8 compliant!](./tests/)
#### Write beautiful code that passes the PEP8 checks.

```
pep8 *.py
```
### [2. Unittests](./models/base_model.py)
#### All your files, classes, functions must be tested with unit tests

#### Running Tests:
The following block will help run the test by running the file through the command line.
```
if __name__ == '__main__':
    unittest.main()
```

### [3. BaseModel](./models/base_model.py)
#### Write a class BaseModel that defines all common attributes/methods for other classes
* Public instance attributes:
    * id: string - assign with an uuid when an instance is created:
         * the goal is to have unique id for each BaseModel 
    *    created_at: datetime - assign with the current datetime when an instance is created
    * updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
* __str__: should print: [<class name>] (<self.id>) <self.__dict__>

### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
#### Previously we created a method to generate a dictionary representation of an instance (method to_dict()).
##### Now it’s time to re-create an instance with this dictionary representation.
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

### [5. Store first object](./console.py)
#### Now we can recreate a BaseModel from another one by using a dictionary representation:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```
It’s great but it’s still not persistent: every time you launch the program you don’t restore all objects created before. So, you will convert the dictionary representation to a JSON string, with this format your BaseModel will be persistent.


#### Now the flow of serialization-deserialization will be:
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
### [6. Console 0.0.1](./console.py)
#### Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./models/user.py)
#### Update your command interpreter (console.py) to have these commands:

* create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
* show: Prints the string representation of an instance based on the class name and id
* destroy: Deletes an instance based on the class name and id (save the change into the JSON file). 
* all: Prints all string representation of all instances based or not on the class name.
* update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
### [8. First User](./models/state.py)
### Write a class User that inherits from BaseModel:
   * Public class attributes:
     * email: string - empty string
     * password: string - empty string
     * first_name: string - empty string
     * last_name: string - empty string
    
##### Update FileStorage to manage correctly serialization and deserialization of User.
##### Update your command interpreter (console.py) to allow show, create, destroy, update and all used with User.
### [9. More classes!](./console.py)
### Write all those classes that inherit from BaseModel:

* State
    * Public class attributes:
      * name: string - empty string 
* City
    * Public class attributes:
      * state_id: string - empty string: it will be the State.id
      * name: string - empty string
* Amenity
    * Public class attributes:
      * name: string - empty string 
* Place
    * Public class attributes:
      * city_id: string - empty string: it will be the City.id
      * user_id: string - empty string: it will be the User.id
      * name: string - empty string
      * description: string - empty string
      * number_rooms: integer - 0
      * number_bathrooms: integer - 0
      * max_guest: integer - 0
      * price_by_night: integer - 0
      * latitude: float - 0.0
      * longitude: float - 0.0
      * amenity_ids: list of string - empty list: it will be the list of Amenity.id later
* Review
    * Public class attributes:
      *  place_id: string - empty string: it will be the Place.id
      *  user_id: string - empty string: it will be the User.id
      *  text: string - empty string


-----------------------

## Authors
* **Sofia Cheung** - [Svcg17](https://github.com/Svcg17)
* **Kenneth Mensah** - [Ken-Mens](https://github.com/Ken-Mens)
