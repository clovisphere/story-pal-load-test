# StoryPal - Load & Performance Test

We're gonna run some performance test on the [StoryPal](https://www.storypal.co/) website using the amazing [Python](https://www.python.org/) programming language. 

### IMPORTANT READ

+ [Taurus](https://gettaurus.org/)
+ [Locust](https://locust.io/)

### ASSUMPTIONS

+ You have [Git](https://git-scm.com/) installed. If you don't, please first install it then come back!

### REQUIREMENTS

Although we could use Python **3.5** and above with both [Taurus](https://gettaurus.org/) and [Locust](https://locust.io/), for this particular project, I have used Python **2.7**. So head to the *download* page on the official [Python website](https://www.python.org/downloads/), and get a copy of Python **2.7** for your system.

We will make heavy use of **pip** and **virtualenv**, you can read about them [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

####STEPS:

Open your *fav* terminal -- if you don't have one, [iTerm2](https://www.iterm2.com/) on the Mac is dope:

1. `$ git clone https://github.com/clovisphere/story-pal-load-test.git`

   The directory should like:
   ```├── app.py
├── quick_test.yml
├── requirements
│   └── requirements.txt
└── stats.csv```

2. `$ CD` into `story-pal-load-test` directory.
3. `$ pip install virtualenv`
4. Create and activate an environment (outside of project directory, preferably):
   +. `$ virtualenv -p /usr/bin/python2.7 my_project`
   +. `$ source performance/bin/activate`
   +. If all went well, name of the current virtual environment will now appear on the left of the prompt, lie: `(my_project)Your-Computer:your_project UserName$)`
   
Now let's install what you will need - the **GOOD STUFF**!

5. `CD` into your `story-pal-load-test` directory (if you weren't in it).
6. `pip install -r  requirements/requirements.txt` to install the Python dependencies you need for this project.

..and that's it! No... You still need to run your test, sorry:-)






