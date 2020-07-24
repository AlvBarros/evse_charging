import setuptools

# Gets readme as a string
with open('README.md', 'r') as fh:
    long_description = fh.read()

# Initialized setup for pip package creation
setuptools.setup(
    name='evse_charging',
    version='0.1',
    scripts=['evse_charging.py'],
    author='Alvaro de Carvalho',
    author_email='alv.barrosc@hotmail.com',
    description='much. Challenge - EVSE/Charging Challenge',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/alvbarros/evse_charging',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)