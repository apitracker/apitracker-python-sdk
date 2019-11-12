from distutils.core import setup

setup(
    name='apitracker_python_sdk',
    packages=['apitracker_python_sdk'],
    version='0.0.2',
    license='MIT',
    description='This is a library to patch python http client to send request to apitracker proxy https://apitracker.com',
    long_description='apitracker is API integration reliability as a service. It provides a network proxy that lets developers adds monitoring, error alerting, auto retry and more to their API integration, all with zero code change. Sign up at https://apitracker.com for a free account',
    author='apitracker',
    author_email='trung@apitracker.com',
    url='https://github.com/trungduyvu/apitracker-python-sdk',
    download_url='https://github.com/trungduyvu/apitracker-python-sdk/archive/0.0.2.tar.gz',
    keywords=['apitracker', 'http', 'proxy'],
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
