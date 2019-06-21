# Tutorial on FSTs and Finite-State Morphology -- JSALT 2019
This tutorial was presented by the Neural Polysynthetic Language Modeling Team at the 2019 JSALT Summer School in Human Language Technology at the École de technologie supérieur in Montréal, Quebec, Canada. It introduces essential FST concepts, with a toy example from English morphology and a challenge problem in Central Alaskan Yup'ik, a polysynthetic language.

## Helpful Resources
  - Slides from the lecture are available [here](https://docs.google.com/presentation/d/1GYEuLNALDkLBQyhIuY6bD6DjctXr0zxJNqNSxM5uz50/edit?usp=sharing)

## Setup
1. Connect to the JSALT cluser following [Yenda's instructions]( https://gist.github.com/jtrmal/6185ddf06d6061a698e800eda208492b) as usual, if desired. You can run this locally as well, provided you have `python3`, `jupyter`, `pip`, and `virtualenv`. Nothing is very computationally expensive. If running locally, skip to step 4.
2. Unlike the other labs, we're going to be running on the login node of the jsalt cluster rather than using qlogin.
5. Create a directory on the file system, if necessary, and `cd` there: `mkdir /export/fs01/[YOUR_USER_NAME]/ && cd /export/fs01/[YOUR_USER_NAME]`.
6.  Clone this git repository and `cd` there: `git clone https://github.com/ColemanHaley/JSALT2019-FST-lab && cd JSALT2019-FST-lab`.`
8. Install the package using the wheel in my home directory: 
```
pip install /export/fs01/ksteimel/hfst.whl
```
8. Run `ip a` to determine what the ip of the sgi cluster is
9. Run `jupyter jupyter notebook --ip=0.0.0.0 --no-browser`
10. You will get a print out like this
```
    To access the notebook, open this file in a browser:
        file:///run/user/2034/jupyter/nbserver-643-open.html
    Or copy and paste one of these URLs:
        http://(master or 127.0.0.1):8889/?token=360a987143374f0a58b41b90b36c912b96ff7dfe1526fa06

```
11. Copy the ip you got from `ip a` into your address bar and paste everything after the closing parenthesis after it. 
```
http://<ip>:8889/?token=360a987143374f0a58b41b90b36c912b96ff7dfe1526fa06
```
10. Open the enclosed Jupyter notebook, and get cracking!
