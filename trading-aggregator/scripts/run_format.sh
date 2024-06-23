#!/bin/bash

isort --old-finders --profile black --line-length 120 . 
black --line-length 120 .