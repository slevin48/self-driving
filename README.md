# self-driving
Hack self-driving [dataset](https://streamlit-self-driving.s3-us-west-2.amazonaws.com/) from Udacity & [app](https://github.com/streamlit/demo-self-driving/blob/master/streamlit_app.py) from Streamlit

Just One image out of the dataset:

![img1.jpg](img1.jpg)

[Youtube - Neural Network driving a car](https://www.youtube.com/watch?v=NJU9ULQUwng&feature=emb_logo&ab_channel=IProgrammerTV)

## Dataset

First Download the [Driving Datasets](https://github.com/udacity/self-driving-car/tree/master/datasets) – Over 10 hours of driving data (LIDAR, camera frames and more)

```
aria2c Ch2_001.tar.gz-692ee7e0c63fb2212bfe4a62a39ce71ee9b16fb3.torrent
```

Untar

```
tar -xf Ch2_001.tar.gz
```

## [udacity-driving-reader](https://github.com/rwightman/udacity-driving-reader)

Build the docker
```
docker build -t udacity-reader .
```
Run the ROS bag reader
```
./run-bagdump.sh -i /data -o /output
```

## [allow-public-access-amazon-bucket](https://havecamerawilltravel.com/photographer/how-allow-public-access-amazon-bucket/)

Access Photos from Python, by building a list ([save list to CSV](https://www.geeksforgeeks.org/python-save-list-to-csv/))
```python
import os
import pandas as pd
list = os.listdir()
df = pd.DataFrame(list,columns=['photo'])
df.to_csv('photos.csv',index=False)
```

Display frames & steering angle with a streamlit app:

![app.jpg](app.jpg)

## [self-driving-car-simulator](https://github.com/udacity/self-driving-car-sim)

![self-driving-sim](https://github.com/udacity/self-driving-car-sim/raw/master/sim_image.png)


Resources:
* https://www.addictivetips.com/ubuntu-linux-tips/download-torrents-from-the-command-line-linux/
* https://github.com/tawnkramer/sdsandbox
* https://github.com/llSourcell/How_to_simulate_a_self_driving_car
* https://www.youtube.com/watch?v=EaY5QiZwSP4&ab_channel=SirajRaval
* https://developer.nvidia.com/blog/deep-learning-self-driving-cars/
