import setuptools

with open('README.md', mode='r') as file:
    long_description = file.read()
    

setuptools.setup(
    name= 'preprocess_sajigera',
    version = '0.0.2',
    author= 'Saji Gera',
    author_email= 'sajigera85@gmail.com',
    description= 'This a preprocessing package.',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent'],
    python_requires = '>=3.5'        
    
)