from setuptools import setup, find_packages


setup(
    name='django-cbv',
    version='0.2',
    description='Django class-based views, backported from Django trunk',
    long_description=open('README.rst').read(),
    author='Bruno Renie',
    author_email='buburno@gmail.com',
    url='https://github.com/brutasse/django-cbv',
    license='BSD',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Framework :: Django',
    ],
)
