from setuptools import setup, find_packages

setup(
    name='simple_weather_cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'weather=simple_weather_cli.weather:get_weather',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple CLI for getting the weather information',
    url='https://github.com/yourusername/simple-weather-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
