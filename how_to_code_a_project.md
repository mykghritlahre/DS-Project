# How to Code a Project Using First Principle Thinking

## What is First Principle Thinking?

First principle thinking is a problem-solving approach that breaks down complex problems into their most fundamental truths and builds up from there, rather than reasoning by analogy or past experience.

### Step 0: First things first

Always create a venv (virtual environment) for your project to manage dependencies and avoid conflicts between packages. You can create a virtual environment using the following command:

```bash
python -m venv [environment_name]
```

Replace `[environment_name]` with the name of your environment. To activate the virtual environment, use:

- On Windows:

```bash
[environment_name]\Scripts\activate
```


- On macOS and Linux:

```bash
source [environment_name]/bin/activate
```

Once activated, you can install packages using pip, and they will be contained within the virtual environment.

### Step 1: Install Required Packages

```bash
pip install -r requirements.txt
```

install any additional packages your project needs.


### 