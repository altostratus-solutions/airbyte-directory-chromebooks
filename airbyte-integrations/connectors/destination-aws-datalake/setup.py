#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk==0.1.6-rc1",
    "boto3",
    "retrying",
    "nanoid",
]

TEST_REQUIREMENTS = ["pytest~=6.1"]

setup(
    name="destination_aws_datalake",
    description="Destination implementation for Aws Datalake.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
