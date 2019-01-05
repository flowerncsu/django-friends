from setuptools import setup, find_packages


setup(
    name = "django-friends",
    version = "0.2.dev1",
    description = "friendship, contact and invitation management for the Django web framework",
    author = "Pinax Team",
    author_email = "team@pinaxprojects.com",
    url = "http://github.com/pinax/django-friends/",
    license="MIT",
    packages = find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data = True,
    package_data = {
        "friends": [
            "templates/notification/*/*.html",
            "templates/notification/*/*.txt",
        ]
    },
    zip_safe = False,
)
