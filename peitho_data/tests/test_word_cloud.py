import os
import pathlib as pl
from unittest import TestCase

from peitho_data import word_cloud


class TestWordCloud(TestCase):
    def test_create_word_cloud_image(self):
        word_cloud.create_word_cloud_image(
            open("peitho_data/tests/pride-and-prejudice.txt", "r").read(),
            "peitho_data/tests/actual_word_cloud.png",
            "peitho_data/tests/alice_mask.png",
        )
        if not pl.Path("peitho_data/tests/actual_word_cloud.png").resolve().is_file():
            raise AssertionError(
                "File does not exist: %s"
                % str("peitho_data/tests/actual_word_cloud.png")
            )
        os.remove("peitho_data/tests/actual_word_cloud.png")
