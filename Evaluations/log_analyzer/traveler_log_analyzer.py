import json
import numpy as np
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs

traced_command_list = ['getUtilizationForPrimitive',
                       'getIntervalDuration',
                       'ganttChartValues',
                       'newMetricData',
                       'drawValues',
                       'getIntervalList',
                       'getIntervalInfo',
                       'getIntervalTraceList']
eventLineParser = re.compile(r'^((?:ENTER)|(?:LEAVE))\s+(\d+)\s+(\d+)\s+(.*)$')
pathParser = re.compile(r'(\s)')

def printAsJSON(entry, f, is_first):
    url = entry['request']['url']
    parsed_url = urlparse(url)
    path = Path(parsed_url.path)
    if path.stem in traced_command_list:
        if is_first == 0:
            is_first = 1
        else:
            f.write(',\n')
        print_dict = dict()
        print_dict['time'] = entry['startedDateTime']
        print_dict['command'] = path.stem
        print_dict.update(parse_qs(parsed_url.query, keep_blank_values=True))
        f.write(json.dumps(print_dict))
    return is_first


def main():
    with open("log.txt", 'r', encoding="utf-16") as file:
        f = open("parsed_requests", "w")
        is_first = 0
        f.write('[\n')
        while line := file.readline():
            t_string = line.split()[0]
            path_match = re.search(r"path=\"((?:[^\"\\]|\\.)*)\"", line)
            if path_match is None:
                continue
            url = path_match.group(1)
            parsed_url = urlparse(url)
            parsed_api = parsed_url.path.split('/')[3]
            parsed_data = parse_qs(parsed_url.query)
            printed_data = {'time': t_string, 'api': parsed_api}
            for key, value in parsed_data.items():
                printed_data[key] = ''.join(value)
            if is_first == 0:
                is_first = 1
            else:
                f.write(',\n')
            f.write(json.dumps(printed_data))
        f.write('\n]')
        f.close()
    print('Done!')


    # with open("log.txt", 'r') as f:
    #     har_parser = HarParser(json.loads(f.read()))
    #     f = open("parsed_requests", "w")
    #     f.write('[\n')
    #     is_first = 0
    #     for entry in har_parser.har_data['entries']:
    #         is_first = printAsJSON(entry, f, is_first)
    #
        # f.write('\n]')
        # f.close()

def generate_random(centroids, points):
    # a portion of total number of points cluster around each centroid
    raw_shares = np.random.rand(centroids)
    shares = (points * raw_shares / np.sum(raw_shares)).astype(int)
    raw_points_collection = []

    for i in shares:
        # random points in each cluster gather around a random centroid
        # a random factor is multiplied to separate clusters
        raw_points_collection.append(
            np.random.rand(i, 2) * np.random.rand() + np.random.rand(2))

    return np.vstack(raw_points_collection)

def hell():
    print('nai')
    centroids = np.array([(1, 2), (3, 4)])
    # lambda k: np.sum(points * np.expand_dims(closest == k, -1), 0) / np.sum(closest == k, 0)

    # print(range(np.shape(centroids, 0)))
    # print(np.sum(centroids, 0))
    # print(np.argmin(centroids,0))
    a = generate_random(2, 5)
    print(a)

if __name__ == '__main__':
    # main()
    hell()