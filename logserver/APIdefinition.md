```
Here's a definition of the API to help you get going :)",
    "documentation": {
        "handlers": {
            "/log_this": {
                "GET": {
                    "examples": [
                        "http://10.24.25.130:8000/log_this?username=bgjerstad&compname=011acboe&stat=on&time=2016-10-20_0229 PM"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "username": {
                            "type": "Basic text / string value"
                        },
                        "compname": {
                            "type": "Basic text / string value"
                        },
                        "stat": {
                            "type": "Basic text / string value"
                        },
                        "time": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            },
            "/get_log": {
                "GET": {
                    "examples": [
                        "http://10.24.25.130:8000/get_log?username=bgjerstad&compname=011acboe"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "username": {
                            "type": "Basic text / string value"
                        },
                        "compname": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            },
            "/get_dup": {
                "GET": {
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    }
                }
            },
            "/db": {
                "GET": {
                    "examples": [
                        "http://10.24.25.130:8000/db?action=clear"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "action": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            },
            "/ex_this": {
                "GET": {
                    "examples": [
                        "http://10.24.25.130:8000/ex_this?username=bgjerstad&action=add"
                    ],
                    "outputs": {
                        "format": "JSON (Javascript Serialized Object Notation)",
                        "content_type": "application/json"
                    },
                    "inputs": {
                        "username": {
                            "type": "Basic text / string value"
                        },
                        "action": {
                            "type": "Basic text / string value"
                        }
                    }
                }
            }
        }
    }
```
