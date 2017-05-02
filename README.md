# Gleamo Raspberry Pi Code

## Getting Started

Install the pip dependencies with `bash ./deps.sh`

Run the tests:

```sh
python main.test.py
```

Or run an integration test to see colors printed:

```sh
python -m __integration.scheduler
```

## Testing the MQ service

Make sure you have RabbitMQ installed to test locally:

```sh
# For OSX
brew install rabbitmq
```

Run each command in a different terminal:

```sh
brew services start rabbitmq # For OSX
python -m __integration.mq
python -m __integration.mq_server
```

## Installing on Raspberry Pi

Run:

```
sudo bash install.sh
sudo bash deps.sh
sudo python demo.py
```
