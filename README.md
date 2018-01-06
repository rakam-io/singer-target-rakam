# target-rakam

Reads [Singer](https://singer.io) formatted data from stdin and persists it to the Rakam API.

## Install

Requires Python 3

```bash
› pip install target-rakam
```

## Use

target-rakam takes two types of input:

1. A config file containing your Rakam client id and access token
2. A stream of Singer-formatted data on stdin

Create config file to contain your Rakam client id and token:

```json
{
  "write_key": "cevc6ajc3b16tcl8616q7hq167u9dhm6c7udgak9beb8ogicvrol331c3fi6uab2",
  "api_url": "http://127.0.0.1:9998"
}
```

```bash
› tap-some-api | target-rakam --config config.json
```

where `tap-some-api` is [Singer Tap](https://singer.io).

---

Copyright &copy; 2017 Rakam
