import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="nicenquickplotlib",
	version="0.0.2",
	author="Matias Senger",
	author_email="m.senger@hotmail.com",
	description="Package to produce nice plots quickly using matplotlib",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/SengerM/nicenquickplotlib",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_data = {
		'': ['*.yaml']
	}
)
