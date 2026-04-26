"""
In this session, you are a tier 1 software vendor designing a product for a
customer for an AV program. The customer's goal is to find their vehicles
efficiently in the world, assuming no prior knowledge. In order to do this, the
customer will use a sensor called a "SquareDAR". This is how the sensor works.
As the name suggests, it can be queried with any geographical square region
(lat, lon, side length) and it returns true or false depending on whether ANY
of their vehicles are within the given GPS square. Use the sensor (mocked by
the provided function) to find the exact location of our vehicles. At the end,
we will discuss the time/space complexities for your code.
"""

# Vehicle locations
VEHICLE_LOCATIONS = [
    (37.389051, -122.066677),
    (48.118849, 11.600665),
    (37.387067, -122.067193),
]


def is_close(p1, p2, eps=1e-6):
  return abs(p1[0] - p2[0]) < eps and abs(p1[1] - p2[1]) < eps


# Returns true if any of the vehicles are within the queried square region
def mock_squaredar_scan(
    lat_min: float,
    lon_min: float,
    side_length: float,
) -> bool:
  return any(lat_min <= lat < lat_min +
             side_length and lon_min <= lon < lon_min + side_length
             for lat, lon in VEHICLE_LOCATIONS)


def make_squares(lat_min: float, lon_min: float, side_length: float):
  hside_length = side_length / 2.0
  return [
      (lat_min + hside_length, lon_min, hside_length),
      (lat_min + hside_length, lon_min + hside_length, hside_length),
      (lat_min, lon_min, hside_length),
      (lat_min, lon_min + hside_length, hside_length),
  ]


def solution():
  # We have to break our big square -> Smaller squares
  # Endpoint for when to stop searching
  LAT_MIN = -180
  LON_MIN = -180
  SIDE_LENGTH_MIN = 0.001
  SIDE_LENGTH_INIT = 360

  # Quadtree-style traversal
  # Time complexity: O(k * log(s init / s min))
  # k: num vehicles
  # s_init: initial side length
  # s_min: minimum side length
  solutions = []
  quadrants = make_squares(LAT_MIN, LON_MIN, SIDE_LENGTH_INIT)

  while quadrants:
    # Pop from queue
    lat_min, lon_min, s = quadrants.pop(0)

    # Stop early if quare doesn't contain vehicle
    if not mock_squaredar_scan(lat_min, lon_min, s):
      continue

    # Add to solutions if side length is at max resolution
    if s < SIDE_LENGTH_MIN:
      solutions.append([lat_min, lon_min])
      continue

    # Keep exploring
    if mock_squaredar_scan(lat_min=lat_min, lon_min=lon_min, side_length=s):
      quadrants += make_squares(lat_min, lon_min, s)

  return solutions


if __name__ == "__main__":
  solutions = solution()
