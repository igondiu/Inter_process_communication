import os
import sys
import requests

sys.path.append(os.path.dirname(os.path.abspath("./tests")))

# DON'T forget to run the docker container to be able to test it correctly


def test_post_message():
    post_url = 'http://0.0.0.0:5000/test_upciti/api/v1/post_message'

    # POST Request :
    the_message = {'message': "Unit test is working !"}
    resp = requests.post(post_url, data=the_message)
    assert resp.status_code == 201
