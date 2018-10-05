# Dataclass properties in Python

This is the supporting repository for "Reconciling Dataclasses And Properties In Python", a blog post published on [my blog](https://blog.florimondmanca.com/reconciling-dataclasses-and-properties-in-python) and [dev.to](https://dev.to).

The various Python files here are the attempts presented in the blog post to implement properties on dataclasses — which is not an intuitive task.

## Usage

To run an interpreter using any of the attempts, you can make use of Python's `-i` command line argument, which starts a shell after running a script:

```bash
$ python -i 3_field.py
>>> # Start doing things with `Vehicle`!
```

## Resources

Official documentation on dataclasses and features used in the blog post:

- [The `@dataclass` decorator](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass)
- [The `field()` function](https://docs.python.org/3/library/dataclasses.html#dataclasses.field)
- [Post-init processing: `__post_init__()`](https://docs.python.org/3/library/dataclasses.html#post-init-processing)
- [Init-only variables: `InitVar`](https://docs.python.org/3/library/dataclasses.html#init-only-variables)
- [PEP-557 -- Data Classes](https://www.python.org/dev/peps/pep-0557/)
