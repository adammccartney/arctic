arctic
=====


For violin, monosynth and polysynth. 

Written as a soundtrack for Becoming Arctic, a film by Robert Platt, May-July 2020. 

[watch the film over at film freeway](https://filmfreeway.com/BecomingArctic)

You can use the password svalbard to watch the full film



## installation 

It's a bit hacky but...

```
git clone git@github.com:adammccartney/arctic.git
cd arctic
python setup.py bdist_wheel
pip install -e .
```

## building the score

+ Todo: refactor so that it can be built with abjad 3.3
  - fix formatting from markups
+ Todo: remove dependencies on mccartney (restucture stylesheets like rill)
+ Todo: copy structure of makefile targets from rill

