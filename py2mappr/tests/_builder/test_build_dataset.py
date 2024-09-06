import pandas as pd
import unittest
from pandas import DataFrame
from py2mappr._layout.scatterplot import ScatterplotLayout
from py2mappr._layout.clustered_scatterplot import ClusteredScatterplotLayout
from py2mappr._layout.geo import GeoLayout
from py2mappr.map import ClusteredLayout, create_layout
from unittest.mock import patch, MagicMock
import pathlib as pl
from py2mappr.publish.publisher import local, set_player_directory

from py2mappr._builder.build_dataset import build_datapoints


def test_string_text_is_converted_from_md():
    datapoint_dict = {
        "id": "test",
        "description": "This is a **test**.",
    }

    datapoint = pd.Series(datapoint_dict)
    dpAttribTypes = {"id": "string", "description": "string"}
    dpRenderTypes = {"id": "default", "description": "text"}

    result = build_datapoints(
        pd.DataFrame([datapoint], index=["description"]),
        dpAttribTypes,
        dpRenderTypes,
    )

    expected = "<p>This is a <strong>test</strong>.</p>"
    assert expected == result[0]["attr"]["description"]


def test_string_default_not_converted_from_md():
    datapoint_dict = {
        "id": "test",
        "description": "This is a **test**.",
    }

    datapoint = pd.Series(datapoint_dict)
    dpAttribTypes = {"id": "string", "description": "string"}
    dpRenderTypes = {"id": "default", "description": "default"}

    result = build_datapoints(
        pd.DataFrame([datapoint], index=["description"]),
        dpAttribTypes,
        dpRenderTypes,
    )

    expected = "This is a **test**."
    assert expected == result[0]["attr"]["description"]


class TestCreateLayout(unittest.TestCase):
    
    def setUp(self):
        # Setup a simple DataFrame as a mock for the datapoints
        self.mock_data_frame = DataFrame({
            'id': [1, 2, 3],
            'x': [0.5, 1.5, 2.5],
            'y': [0.5, 1.5, 2.5]
        })
    
    def test_create_clustered_layout(self):
        layout = create_layout(self.mock_data_frame, "clustered")
        self.assertIsInstance(layout, ClusteredLayout)

    def test_create_scatterplot_layout(self):
        layout = create_layout(self.mock_data_frame, "scatterplot")
        self.assertIsInstance(layout, ScatterplotLayout)

    def test_create_clustered_scatterplot_layout(self):
        layout = create_layout(self.mock_data_frame, "clustered-scatterplot")
        self.assertIsInstance(layout, ClusteredScatterplotLayout)

    def test_create_geo_layout(self):
        layout = create_layout(self.mock_data_frame, "geo")
        self.assertIsInstance(layout, GeoLayout)

    def test_invalid_layout_type(self):
        with self.assertRaises(ValueError):
            create_layout(self.mock_data_frame, "invalid")



class TestLocalFunction(unittest.TestCase):
    @patch('py2mappr.publish.local_worker.local_worker')
    def test_local_decorator_with_default_web_dir(self, mock_local_worker):
        # Setup
        test_directory = pl.Path("/fake/path")
        set_player_directory(test_directory)

        # Mock the return value of the worker
        mock_local_worker.return_value = {"result": "success"}

        # Prepare the data to pass to the worker
        data = {"web_dir": test_directory}

        # Get the function to be decorated by local
        worker_function = local()(data)

        # Ensure the worker was called correctly
        mock_local_worker.assert_called_once_with(web_dir=test_directory, PORT=8080)

        # Assert the return value from the worker
        self.assertEqual(worker_function, {"result": "success"})

    @patch('py2mappr.publish.local_worker.local_worker')
    def test_local_decorator_with_custom_web_dir(self, mock_local_worker):
        # Setup a custom web directory
        custom_web_dir = pl.Path("/custom/web/dir")

        # Mock the return value of the worker
        mock_local_worker.return_value = {"result": "success"}

        # Prepare the data to pass to the worker
        data = {}

        # Get the function to be decorated by local with a custom web_dir
        worker_function = local(web_dir=custom_web_dir)(data)

        # Ensure the worker was called correctly
        mock_local_worker.assert_called_once_with(web_dir=custom_web_dir, PORT=8080)

        # Assert the return value from the worker
        self.assertEqual(worker_function, {"result": "success"})

    @patch('py2mappr.publish.local_worker.local_worker')
    def test_local_decorator_with_custom_port(self, mock_local_worker):
        # Setup a custom web directory and port
        custom_web_dir = pl.Path("/custom/web/dir")
        custom_port = 9090

        # Mock the return value of the worker
        mock_local_worker.return_value = {"result": "success"}

        # Prepare the data to pass to the worker
        data = {}

        # Get the function to be decorated by local with a custom web_dir and port
        worker_function = local(web_dir=custom_web_dir, PORT=custom_port)(data)

        # Ensure the worker was called correctly with the custom port
        mock_local_worker.assert_called_once_with(web_dir=custom_web_dir, PORT=custom_port)

        # Assert the return value from the worker
        self.assertEqual(worker_function, {"result": "success"})