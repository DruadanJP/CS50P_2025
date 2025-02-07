import sys
from os.path import getsize


def main():
    coordinates_tuple = (42.367, -71.115)
    coordinates_list = [42.367, -71.115]
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")

main()