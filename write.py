"""Write a stream of close approaches to CSV or to JSON.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w', newline="") as outfile:
        close_approach_writer = csv.writer(outfile, delimiter=',')
        close_approach_writer.writerow(fieldnames)
        for i in results:
            close_approach_writer.writerow([i.time_str, i.distance, i.velocity, i.neo.designation, i.neo.name, i.neo.diameter, i.neo.hazardous])


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename, 'w') as outfile:
        my_list = []
        for i in results:
            my_dict = {}
            my_dict['datetime_utc'] = i.time_str
            my_dict['distance_au'] = i.distance
            my_dict['velocity_km_s'] = i.velocity
            my_dict['neo'] = {}
            my_dict['neo']['designation'] = i.neo.designation
            my_dict['neo']['name'] = i.neo.name
            my_dict['neo']['diameter_km'] = i.neo.diameter
            my_dict['neo']['potentially_hazardous'] = i.neo.hazardous
            my_list.append(my_dict)
        json.dump(my_list, outfile, indent=2)
