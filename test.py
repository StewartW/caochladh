#!/usr/bin/env python3

from unittest.mock import MagicMock
from lambda import handler


if __name__ == '__main__':

    event = {'instance-id': 'i-033d58df5ffaf79c5', 'instance-action': 'terminate'}
    context = MagicMock()
    context.function_name = 'instance-termination'

    handler(event, context)
