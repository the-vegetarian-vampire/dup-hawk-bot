To get started contributing to this project, you'll first need to set up your development environment.

```
git clone https://github.com/cyfrin/dup-hawk
cd dup-hawk
```

Then, setup your environment
```
poetry install
```

### Optional

You can also install the package in editable mode.

```
pip install -e .
```

The `pip install -e .` command installs our package in "editable" mode. This means that any changes you make to the code will be reflected in the package you import in your own code.

This would be if you want to run make changes and test them out on your own code in another project. 


# Uploading to PyPI 

_For maintainers only. You can view the [docs](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) to learn more._ 

_Note: `setup.py sdist` is deprecated. Use `python3 -m build` instead._

```
poetry publish --build -u __token__ -p $PYPI_API_TOKEN
```

*If you don't have an API key, make one, and give it access to your whole project, then delete it and make a new restricted one.*

Right now, we have our GitHub actions setup so that every release we push we automatically upload to PyPI.
