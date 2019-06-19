# Tutorial on FSTs and Finite-State Morphology -- JSALT 2019
This tutorial was presented by the Neural Polysynthetic Language Modeling Team at the 2019 JSALT Summer School in Human Language Technology at the École de technologie supérieur in Montréal, Quebec, Canada. It introduces essential FST concepts, with a toy example from English morphology and a challenge problem in Central Alaskan Yup'ik, a polysynthetic language.

## Helpful Resources
  - Slides from the lecture are available [here]()

## Setup
1. Connect to the JSALT cluser following [Jan's instructions]( https://gist.github.com/jtrmal/6185ddf06d6061a698e800eda208492b) as usual, if desired. You can run this locally as well, provided you have `python3`, `jupyter`, `pip`, and `virtualenv`. Nothing is very computationally expensive. If running locally, skip to step 4.
2. Unlike the other labs, we're going to be running on the login node of the jsalt cluster rather than using qlogin.
3. Sign up in the attached google sheets file with the port number you're going to be using
4. Run ssh with port forwarding to your specified port. 
    `ssh -i jsalt.pem -L 127.0.0.1:<port>:127.0.0.1:<port> ec2-52-205-171-112.compute-1.amazonaws.com`

5. Create a directory on the file system, if necessary, and `cd` there: `mkdir /export/fs01/[YOUR_USER_NAME]/ && cd /export/fs01/[YOUR_USER_NAME]`.
6.  Clone this git repository and `cd` there: `git clone https://github.com/ColemanHaley/JSALT2019-FST-lab && cd JSALT2019-FST-lab`.
7. Create a virtual environment and activate it: `virtualenv env && source env/bin/activate`. If `virtualenv` is not installed on the cluster, try running `pip install virtualenv`. If this is acting up, maybe try troubleshooting based on the steps [here](https://gist.github.com/pmichel31415/33722f12665eedcccb251d14313bf680)? 
8. Install the requirements: `pip install -r requirements.txt`.
9. Run `jupyter notebook`. If running on the cluster, you should specify your chosen port number. e.g. `jupyter notebook --port <port>`
10. Open the enclosed Jupyter notebook, and get cracking!








