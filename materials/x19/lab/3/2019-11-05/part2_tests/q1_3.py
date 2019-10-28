test = {
  'name': 'Question 1_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(parameters)
          3
          >>> np.isclose(parameters.item(0), 0.8343076972837598)
          True
          >>> np.allclose(parameters, [0.8343077, 0.09295728, -1.56652097])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
