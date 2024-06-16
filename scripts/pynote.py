#!/usr/bin/env python3
import os
import sys
import argparse
import importlib.util
from docutils.core import publish_string


def convert(input_path, output_path):
  # Load python module
  module_dir = os.path.dirname(input_path)
  module_name = os.path.splitext(os.path.basename(input_path))[0]
  spec = importlib.util.spec_from_file_location(module_name, input_path)
  module = importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)

  # Convert notebook
  rst_content = module.__doc__
  html_content = publish_string(rst_content, writer_name='html')
  output = open(output_path, "w")
  output.write(html_content.decode("utf-8"))
  output.close()


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--input_path")
  parser.add_argument("--output_path")
  args = parser.parse_args()
  convert(args.input_path, args.output_path)
