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

#### STEPS:

Open your *fav* terminal -- if you don't have one, [iTerm2](https://www.iterm2.com/) on the Mac is dope:

1. `$ git clone https://github.com/clovisphere/story-pal-load-test.git`

   The directory's content should look like:
   
   ```
   ├── app.py
   ├── img
   │     └── test_stats.png
   ├── quick_test.yml
   ├── requirements
   │     └── requirements.txt
   └── stats.csv
    ```

2. `$ CD` into `story-pal-load-test` directory.
3. `$ pip install virtualenv`
4. Create and activate a virtual env (outside of project directory, preferably):

```
   + `$ virtualenv -p /usr/bin/python2.7 my_project`
   + `$ source my_project/bin/activate`
```

If all went well, the name of the current virtual environment will now appear on the left of the prompt, like: `(my_project)Your-Computer:your_project UserName$)`
   
Now let's install what you will need for the performance test a.k.a the **GOOD STUFF**!

5. `$ CD` into your `story-pal-load-test` directory (if you weren't in it).
6. `$ pip install -r  requirements/requirements.txt` to install the Python dependencies you need for this project.

..and that's it! No... You still need to run your tests, right?

If you open, the **app.py** file, you will see:

```python
STUDENTS = [
    {
        'username': '',
        'password': ''
    }
]

GUARDIANS = [
    {
        'username': '',
        'password': ''
    }
]
```
You may wanna read (more) about Python data structure, here is a good [link](https://docs.python.org/2/tutorial/datastructures.html). The only thing you need to do is pass the correct/valid username and password -- if you wanna test with different usernames and passwords, you can, just add additional ones, like:

```python
STUDENTS = [
  {'username': '', 'password': ''},
  {'username': '', 'password': ''},
  {'username': '', 'password': ''}
  .
  .
  .
]
```
You may also wanna tinker with `quick_test.yml` file

```
execution:
- executor: locust
  concurrency: 100 # number of target concurrent virtual users
  hold-for: 1m  # test duration
  scenario: test # test to run (see 'scenarios')

scenarios:
  test:
    default-address: https://www.storypal.co  # test endpoint
    script: app.py # python script that contains your locust load test

reporting:
  - module: final-stats
    summary: true  # overall samples count and percent of failures
    percentiles: true  # display average times and percentiles
    failed-labels: false  # provides list of sample labels with failures
    test-duration: true  # provides test duration
    dump-csv: stats.csv
```
Self explanatory, I believe!

### RUN TEST:

`$ bzt quick_test.yml`

**Note:** `$` denotes the **shell prompt** on Mac/Linux (so do not type it when running command) 

That's it.. if you did things well, you'd see something like:

![Example - Taurus/Console](img/test_stats.png?raw=true "some stats")




