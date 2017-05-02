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

Create a new user for connecting to the rabbitmq instance from outside of localhost. Head up, this is just for testing:

```sh
# On OSX, rabbitmqctl is in /usr/local/sbin/rabbitmqctl
rabbitmqctl delete_user guest
rabbitmqctl add_user gleamo gleamo
rabbitmqctl set_permissions gleamo "commands" ".*" ".*"
```

Then, add a configuration file in `/usr/local/etc/rabbitmq/rabbitmq.conf`:

```erlang
[
  {rabbit, [
    {tcp_listeners, [
      {"::", 5672}
    ]}
  ]}
].
```

On OSX, you'll need to remove the following like from `/usr/local/etc/rabbitmq/rabbitmq-env.conf`:

```
NODE_IP_ADDRESS=127.0.0.1
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
