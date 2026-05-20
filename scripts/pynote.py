#!/usr/bin/env python3
import argparse
from pathlib import Path


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--input_path", required=True)
  parser.add_argument("--output_path", required=True)
  args = parser.parse_args()

  input_path = Path(args.input_path)
  output_path = Path(args.output_path)
