#!/usr/bin/env python
# coding: utf-8

# Copyright (c) me.
# Distributed under the terms of the Modified BSD License.

"""
TODO: Add module docstring
"""

from ipywidgets import DOMWidget
from traitlets import Unicode, Int, Dict
from ._frontend import module_name, module_version


class ExampleWidget(DOMWidget):
    """TODO: Add docstring here"""

    _model_name = Unicode("ExampleModel").tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode("ExampleView").tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    # widget state that is synced between Python and JavaScript

    data = Dict({}).tag(sync=True)
    height = Int(0).tag(sync=True)

    def __init__(self, data, height=600, **kwargs):
        super().__init__(**kwargs)

        self.data = data
        self.height = height
