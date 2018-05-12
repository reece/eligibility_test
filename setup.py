from setuptools import setup

setup(
    name="Eligibility Test",
    description="""A fun thought experiment""",
    long_description=open("README.md").read(),
    install_requires=[
        "flask",
        "jsonschema",
    ]
)
