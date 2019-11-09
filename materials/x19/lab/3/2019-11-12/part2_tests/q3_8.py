test = {
  'name': 'Question 3_8',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Make sure most_recent_wait is a single value
          >>> isinstance(most_recent_wait, float)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(most_recent_wait, 89.28185919744949)
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
