<div align="center">

<img src="./image/unit-7 .png">

## Unit-7
##### webserver for micropython made easy 🐍


</div>

### What is it ❓

A framework for developing webservers on microcontrollers running micropython 🐍

```that's a  lot of micro we got there 🤔```


### Our Goal 🥅

The goal of this project is to create a framework for micropython which would ease the webserver developement process

p.s. : please look [this discussion](https://github.com/TakshakRamteke/Unit-7/discussions/2) to get a more clear idea


### Setup guide 🔌

```Assuming that you have micropython already setup ```

1. Clone this repo via ```git clone https://github.com/TakshakRamteke/Unit-7.git```
1. Change directory with ```cd Unit-7```
1. Copy the `u7.py` & `boot.py` file from src to your microcontroller
1. Change the ssid and password in `boot.py`

### Creating a Server ✨ 

```After you've setted up this project you can create a server by```

1. Import `u7` by using `from u7 import U7`

1. Create a server using 

```py
app = U7
app.run(app.render("your html file"))

```

### Licence 📜

This project is [licenced under MIT]("./LICENCE")


