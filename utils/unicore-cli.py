#!/usr/bin/env python3
########################################################################
# unicore-cli.py - Command-line Utilities                              #
# Copyright (C) 2024 Kenny Ngo / UnicoreFW / IIPTech.info              #
#                                                                      #
# This file is part of UniCoreFW.                                      #
# UniCore is free software: you can redistribute it and/or modify      #
# it under the terms of the [LGPL-3.0/MPL-2.0] as published by         #
# the Free Software Foundation.                                        #
# You should have received a copy of the [LGPL-3.0/MPL-2.0] license    #
# along with UniCoreFW. If not, see https://www.gnu.org/licenses/.     #
########################################################################

import os
import glob
import argparse
import sys
import re

# Set the base directory path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Ensure the 'src' directory is in sys.path for unicore imports
# sys.path.insert(0, os.path.join(BASE_DIR, '../src'))
from ..src.unicore import unicore

def _test_examples(args):
    """
    Runs example files based on the provided argument.
    If '_all_' is provided, runs all example files.
    """
    if not args:
        print("Usage: unicore-cli --test=examples <method>")
        return

    arg = unicore.first(args)
    examples_path = os.path.join(BASE_DIR, '../examples')

    if unicore.isString(arg):
        if arg == '_all_':
            # Run all example files matching the pattern
            for file_path in glob.glob(os.path.join(examples_path, 'ex_*.py')):
                print(f"\nExecuting {file_path}")
                run_example(file_path)
        else:
            file_path = os.path.join(examples_path, f'ex_{arg}.py')
            if os.path.exists(file_path):
                print(f"Executing {file_path}")
                run_example(file_path)
            else:
                print(f"Error: Example file '{file_path}' not found.")
    else:
        print("Error: Invalid argument. Expected a string.")

def run_example(file_path):
    """
    Safely executes a Python example file by importing it as a module.
    """
    try:
        with open(file_path, 'r') as f:
            exec(f.read()) 

    except Exception as e:
        print(f"Error executing {file_path}: {e}")

def parse_args():
    """
    Parses command-line arguments with `--name=value` format and additional positional arguments.

    Returns:
        tuple: A dictionary containing key-value pairs from `--name=value` arguments
               and a list of positional arguments.
    """
    parser = argparse.ArgumentParser(
        description='Parse --name=value command-line arguments and additional positional arguments.',
        allow_abbrev=False,
        add_help=False
    )

    known_args, unknown_args = parser.parse_known_args()

    # Process key-value arguments with `--name=value` format
    def process_arg(arg):
        if arg.startswith('--') and '=' in arg[2:]:
            key, value = arg[2:].split('=', 1)
            if key:
                return key, value
            else:
                parser.error(f"Invalid argument format: '{arg}'. Key cannot be empty.")
        else:
            return arg

    # Parse each argument: store key-value pairs and positional arguments separately
    key_value_dict = {}
    positional_args = []

    for arg in unknown_args:
        processed = process_arg(arg)
        if isinstance(processed, tuple):
            key, value = processed
            key_value_dict.setdefault(key, []).append(value)
        else:
            positional_args.append(processed)

    # Finalize dictionary by collapsing single-item lists
    final_key_value_dict = unicore.mapObject(key_value_dict, lambda v: v[0] if len(v) == 1 else v)

    return final_key_value_dict, positional_args

def main():
    """
    Unicore Command-Line Utilities for maintaining UnicoreFW.
    """
    try:
        actions, args = parse_args()
    except SystemExit as e:
        # argparse uses sys.exit(), which raises SystemExit
        raise e

    if not actions:
        print("No arguments were provided.")
        return

    for action, action_invoker in actions.items():
        # Sanitize action and action_invoker to prevent unintended execution
        function_name = f"_{re.sub(r'[^a-zA-Z0-9]', '', action)}_{re.sub(r'[^a-zA-Z0-9]', '_', action_invoker)}"
        function = globals().get(function_name)

        if function:
            print(f"Invoking function {function_name}")
            function(args)
            break
        else:
            print(f"Error: Command '{action}={action_invoker}' not found.")

if __name__ == '__main__':
    main()