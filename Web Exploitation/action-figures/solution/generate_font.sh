#!/bin/bash

filename=$1

fontforge -c 'font = fontforge.font(); font.copyright = "DUMMY FONT"; font.generate("'$filename'")'
