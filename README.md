![Chamasifier](pictures/header.png)

### Table of contents

<!--ts-->

-   [What is Chamasifier?](#what-is-Chamasifier?)
-   [Installation](#installation)
-   [Features](#features)
-   [Demo](#demo)
    -   [Chamasifier](#chamasifier)
    -   [Web Interface](#web-interface)
-   [Contributing](#contributing)
-   [Contributers](#contributers)
-   [License](#license)
<!--te-->

### What is Chamasifier?

[CHAMASIFIER](http://ec2-3-17-203-44.us-east-2.compute.amazonaws.com:8080/) a.k.a CHA-kka MA-nga clas-SIFIER is a machine learning project which can identify the two of the fruits 'Chacka' and 'Manga'(JackFruit and Mango).The ML algorithm used here is Convolutional Neural Network. This algorithm can classify images based on the features.Tensorflow-Keras library is used here for the purpose of creation,training and testing of the model.For the website implementation we used the flask library of python.

### Installation

Python and pip should be installed in the system.
Can be installed by using

```sudo apt install python python-pip```

Other requirements are written in the [requirements.txt](requirements.txt) file.
It can be installed using 

```pip install -r requirements.txt```


### Features

The main features of Chamasifier are,

-   Trained with over 600 images,
-   has an accuracy of ~70%,
-   it has 3 convolution layers and 3 pooling layers,
-   2 dense hidden layers,
-   rmsprop optimization.

### Demo

#### Chamasifier

Click [here](http://ec2-3-17-203-44.us-east-2.compute.amazonaws.com:8080/) to see the working project.

#### Web Interface

![Web Interface Image](pictures/web1.png)

![Web Interface Image](pictures/web2.png)

![Web Interface Image](pictures/web3.png)

### Contributing

click [here](contributing.md) to see the details.



### License

This project is licensed under the permissive open-source [MIT license](LICENSE).
