from setuptools import setup

__version__ = "0.4.1"
url = "https://github.com/ntt123/vietTTS"

install_requires = [
    "dm-haiku",
    "einops",
    "fire",
    "gdown",
    "jax",
    "jaxlib",
    "librosa",
    "optax",
    "tabulate",
    "textgrid @ git+https://github.com/kylebgorman/textgrid.git",
    "tqdm",
    "matplotlib"
]
setup_requires = []
tests_require = []

setup(
    name="vntts",
    version=__version__,
    description="",
    author="",
    url=url,
    keywords=["text-to-speech", "vietnamese", "tts"],
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    packages=["vntts"],
    python_requires=">=3.7",
)
