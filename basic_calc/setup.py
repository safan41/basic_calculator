from distutils.core import setup
import pyinstaller
setup(
    name='basic_calc',
    version='0.1',
    packages=['basic_calc',],
    license='MIT License',
    long_description=open('README.txt').read(),
    console=['_init_.py']
)

