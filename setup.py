from setuptools import setup

setup(
    name="pyowa-buildout",
    version="dev",
    description="Buildout Example for Pyowa presentation",
    author="Matthew J. Morrison",
    author_email="mattj.morrison@gmail.com",
    package_dir={'':'src'},
    packages=('sample',),
    install_requires = (
        
    ),
    entry_points = ("""
        [console_scripts]
        versions=sample:show_versions
    """)
)
