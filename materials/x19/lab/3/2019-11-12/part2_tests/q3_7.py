test = {
  'name': 'Question 3_7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure two_minutes_wait is a single value
          >>> isinstance(two_minutes_wait, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(two_minutes_wait, 67.52659892156797)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
