
# Introduction

This repository was built to showcase Vehicle Collision Detection using TFOD framework. Here we used ssd_mobilenet_v1_coco Algorithm from TFOD model zoo.

Idea was to develop Collision Detection which could alert driver before there is a Collision. Here we have create a Area of Interest if any Vehicle whose bounding boxes cordinate falls inside this Area of Interest and the distance between the two points is below thresh hold in that case we alert the driver.

To see other models from Model Zoo please use link (https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md)

### Output

![](ezgif.com-gif-maker.gif)




## Run Locally

Clone the project

```bash
  git clone https://github.com/nabarunbaruaAIML/Vehicle-Collision-Detection.git
```

Go to the project directory

```bash
  cd Vehicle-Collision-Detection
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python3 Collision_detection.py
```

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
