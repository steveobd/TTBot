from setuptools import setup,find_packages

setup(name='TTBot',
        packages=find_packages(include=['ttbot', 'ttbot.*']),
        version='3.1',
        author='01ly',
        author_email='apisite@126.com',
        description="TTBot",
        url='https://github.com/steveobd/TTBot',
        install_requires=[
        'opencv-python==4.1.0.25',
        'PyExecJS==1.5.1',
        'pymongo==3.7.1',
        'requests==2.20.0',
        'selenium==3.14.1',
        'urllib3==1.24.2',
        'validators==0.13.0',
        'w3lib==1.19.0',
        'bs4'


        ],
        )