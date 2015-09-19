#!/usr/bin/env python3

import argparse
from urllib.request import urlopen
import json
import sys
import time

DEFAULT_URL = 'http://listen.di.fm/public2'
DEFAULT_DELAY = 0.5


def main():
    parser = _get_parser()
    args = parser.parse_args()

    fp = urlopen(args.url)
    stations = json.loads(fp.read().decode('utf-8'))
    fp.close()

    entries = []
    for station in stations:
        key = station['key']
        name = station['name']
        playlist = station['playlist']

        time.sleep(args.delay)
        fp = urlopen(playlist)
        try:
            pls = fp.read().decode('utf-8')
        finally:
            fp.close()

        streams = _read_pls_streams(pls)
        for stream in streams:
            entries.append((key, name, stream))

    if isinstance(args.output, str):
        output = open(args.output, 'w')
    else:
        output = sys.stdout

    output.write('#EXTM3U\n')

    for entry in entries:
        key, name, stream = entry
        output.write('#EXTINF:-1,%s\n' % name)
        output.write(stream + '\n')


def _read_pls_streams(pls):
    streams = []
    for line in pls.splitlines():
        if line.startswith('File'):
            _, url = line.split('=', 1)
            streams.append(url)
    return streams


def _get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', default=DEFAULT_URL,
                        help='Playlist download URL')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-d', '--delay', type=float, default=DEFAULT_DELAY,
                        help='Time to delay between fetching playlists')
    return parser

if __name__ == '__main__':
    main()
