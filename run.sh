docker run --rm --name="property-testing-lesson" --net="host" -v `pwd`:/home -i -t property-testing-lesson pytest -s -p no:logging
