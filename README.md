# Tutorial on FSTs and Finite-State Morphology -- JSALT 2019
This tutorial was presented by the Neural Polysynthetic Language Modeling Team at the 2019 JSALT Summer School in Human Language Technology at the École de technologie supérieur in Montréal, Quebec, Canada. It introduces essential FST concepts, with a toy example from English morphology and a challenge problem in Central Alaskan Yup'ik, a polysynthetic language.

## Helpful Resources
  - Slides from the lecture are available [here]()

## Setup
1. Connect to the JSALT cluser following [Jan's instructions]( https://gist.github.com/jtrmal/6185ddf06d6061a698e800eda208492b) as usual, if desired. You can run this locally as well, provided you have `python3`, `jupyter`, `pip`, and `virtualenv`. Nothing is very computationally expensive. If running locally, skip to step 4.
2. Login into an interactive session: `qlogin -q all.q`.
3. Create a directory on the file system, if necessary, and `cd` there: `mkdir /export/fs01/[YOUR_USER_NAME]/ && cd /export/fs01/[YOUR_USER_NAME]`.
4.  Clone this git repository and `cd` there: `git clone https://github.com/ColemanHaley/JSALT2019-FST-lab && cd JSALT2019-FST-lab`.
5. Create a virtual environment and activate it: `virtualenv env && source env/bin/activate`. If `virtualenv` is not installed on the cluster, try running `pip install virtualenv`. If this is acting up, maybe try troubleshooting based on the steps [here](https://gist.github.com/pmichel31415/33722f12665eedcccb251d14313bf680)? 
6. Install the requirements: `pip install -r requirements.txt`.
7. Run `jupyter notebook`. How to do on cluster? Why would anyone do this on cluster, actually?
8. Open the enclosed Jupyter notebook, and get cracking!








