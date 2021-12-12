from setuptools import setup, find_packages


with open('./LICENSE') as description:
    long = description.read()
setup(
    name='UNKnownDB',
    version='0.0',
    author='CleaverCreator',
    author_email='liuhanbo333@icloud.com',
    packages=find_packages(),
    zip_safe=False,
    platforms=['Linux'],
    install_requires=[],
    description='A new DB',
    license='A2.0',
    url='https://github.com/CleverCreater/UNKnownDB',
    long_description=long
)
