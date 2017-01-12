server = {
    "port": 8000,
    "token": "some-token",
    "hook_post_url": "http://some.default-hook.url/token=some-other-token"
}

hooks = {
    "/some-path": {
        "element_identifier_type": "class",
        "element_class": "someClass",
        "element_url": "http://www.example.com",
        "hook_post_url": "http://some.hook.url/token=some-other-token"
    }
}
