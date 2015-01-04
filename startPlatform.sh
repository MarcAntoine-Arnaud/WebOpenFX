#!/bin/bash

python render/runRender.py &
python catalog/runCatalog.py &
python client/runClient.py &
