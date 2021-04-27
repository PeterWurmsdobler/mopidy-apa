****************************
Mopidy-APA
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-APA
    :target: https://pypi.org/project/Mopidy-APA/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/github/workflow/status/PeterWurmsdobler/mopidy-apa/CI
    :target: https://github.com/PeterWurmsdobler/mopidy-apa/actions
    :alt: CI build status

.. image:: https://img.shields.io/codecov/c/gh/PeterWurmsdobler/mopidy-apa
    :target: https://codecov.io/gh/PeterWurmsdobler/mopidy-apa
    :alt: Test coverage

Mopidy extension to control Audio Power Amplifier


Prerequisites
=============

Raspbian and Mopidy installation

Follow the instructions on https://docs.mopidy.com/en/latest/installation/raspberrypi/ to install both the Raspberry PI Debian based operating system as well as Mopidy.

PIP support

Raspberry buster comes with python3.7, but not with pip, so::

    sudo apt install python3-pip

GPIO support::

    sudo python3.7 -m pip install Rpi.GPIO
    sudo python3.7 -m pip install gpiozero


Installation
============

For now, until there is a pypi package available::

    sudo apt install git
    git clone https://github.com/PeterWurmsdobler/mopidy-apa.git
    cd mopidy-apa
    sudo python3.7 ./setup.py install


Configuration
=============

Before starting Mopidy, you must add configuration for
Mopidy-APA to your Mopidy configuration file::

    [apa]
    # TODO: Add example of extension config


Project resources
=================

- `Source code <https://github.com/PeterWurmsdobler/mopidy-apa>`_
- `Issue tracker <https://github.com/PeterWurmsdobler/mopidy-apa/issues>`_
- `Changelog <https://github.com/PeterWurmsdobler/mopidy-apa/blob/master/CHANGELOG.rst>`_


Credits
=======

- Original author: `Peter Wurmsdobler <https://github.com/PeterWurmsdobler>`__
- Current maintainer: `Peter Wurmsdobler <https://github.com/PeterWurmsdobler>`__
- `Contributors <https://github.com/PeterWurmsdobler/mopidy-apa/graphs/contributors>`_
