# Gleamo Raspberry Pi Code

## Getting Started

Install the pip dependencies with `bash ./deps.sh`

Run the tests:

```sh
python main.test.py
```

Or run an integration test to see colors printed (see the next section for configuration options):

```sh
python -m __integration.scheduler
```

## Configuration

By default, there is a `config.example.cfg` file and a `config.local.cfg` value with
default values. Copy the example:

```sh
cp config.example.cfg config.cfg
```

Change the values in `./config.cfg` and `./config.local.cfg` to fit your needs.

## Testing the MQ service

See [the Gleamo MQ knowledgebase](https://github.com/Gleamo/gleamo-mq) for
instructions on setting up your local environment.

Run each command in a different terminal:

```sh
brew services start rabbitmq # For OSX
python -m __integration.mq
python -m __integration.mq_server
```

## Installing on Raspberry Pi

Run:

```sh
sudo bash install.sh
sudo bash deps.sh
sudo python demo.py
# or
sudo python main.py
```
