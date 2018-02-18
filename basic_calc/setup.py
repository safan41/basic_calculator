from distutils.core import setup
import py2exe
setup(
    name='basic_calc',
    version='0.1',
    packages=['basic_calc',],
    license='MIT License',
    long_description=open('README.txt').read(),
    console=['_init_.py']
)

