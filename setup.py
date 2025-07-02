---

### `setup.py`
```python
from setuptools import setup, find_packages

setup(
    name="elavon_omni_sdk",
    version="0.1.0",
    description="Python SDK for Elavon Omni Commerce Gateway",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    python_requires=">=3.7",
)