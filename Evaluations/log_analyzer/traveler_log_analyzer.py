import json
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
#     test_string = "honeyhello path_nai"
#     test_string = "2022-03-09T01:31:13.620350+00:00 heroku[router]: at=info method=GET " + \
#                   "path=\"/datasets/0c366d78-eb68-405f-819e-096b9f2729a6/getUtilizationForPrimitive?bins=662&begin=47907181&end=1400844060&isCombine=true" + \
#                   "&utilType=utilization&primitive=all_primitives&duration_bins=220\" host=traveler-integrated.herokuapp.com " + \
#                   "request_id=2e8ff26d-16fd-4e52-b2b9-d8d16ad65360 fwd=\"67.1.161.153\" dyno=web.1 connect=0ms service=313ms status=200 bytes=592297 " + \
#                   "protocol=https"
#     txt = "The rain in Spain"
#     x = re.search(r"path=\"((?:[^\"\\]|\\.)*)\"", test_string)
#     if x is not None:
#         print(x.group(1))
#     else:
#         print('not found')
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


if __name__ == '__main__':
    main()