from setuptools import find_packages, setup

setup(
    author="Pratik Indap",
    author_email="nunna@yourbusiness.com",
    description="""A fun thought experiment""",
    long_description=open("README.md").read(),
    name="Eligibility Test",
    packages=["eligibility_test"],
    package_data={"": ["_data/*"]},
    url="https://github.com/pratikindap/eligibility_test",

    install_requires=[
        "flask",
        "jsonschema",
    ],
)
