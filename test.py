import argparse

from google.cloud import logging


def list_entries(logger_name):
    """Lists the most recent entries for a given logger."""
    logging_client = logging.Client()
    logger = logging_client.logger(logger_name)

    print('Listing entries for logger {}:'.format(logger.name))

    for entry in logger.list_entries():
        timestamp = entry.timestamp.isoformat()
        print('* {}: {}'.format
              (timestamp, entry.payload))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'logger_name', help='Logger name', default='example_log')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('list', help=list_entries.__doc__)

    args = parser.parse_args()

    if args.command == 'list':
        list_entries(args.logger_name)
